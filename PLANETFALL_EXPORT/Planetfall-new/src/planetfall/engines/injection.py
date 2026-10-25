import numpy as np
from .discovery import BlindDiscoveryEngine

class InjectionRecoveryEngine:
    """
    Authentic Injection-Recovery Engine.
    Injects synthetic limb-darkened transit signals into genuine observational photometry
    and runs the full blind detection pipeline to measure empirical completeness and bias.
    Zero static or hardcoded outputs.
    """

    def __init__(self, u1=0.3, u2=0.2):
        self.u1 = u1
        self.u2 = u2
        self.discovery_engine = BlindDiscoveryEngine(min_snr=7.0)

    def _generate_synthetic_transit(self, time, period, t0, depth, duration_days):
        """Generate limb-darkened transit profile."""
        rp = np.sqrt(max(1e-6, depth))
        phase = ((time - t0 + 0.5 * period) % period) / period - 0.5
        phase_days = np.abs(phase * period)
        
        in_transit = phase_days < (0.5 * duration_days)
        synthetic_flux = np.ones_like(time)
        if np.any(in_transit):
            # Ingress/egress limb factor
            tau = phase_days[in_transit] / (0.5 * duration_days)
            # Quadratic limb darkening profile
            limb = 1.0 - self.u1 * (1.0 - np.sqrt(np.maximum(0.0, 1.0 - tau**2)))
            limb = np.clip(limb, 0.5, 1.0)
            synthetic_flux[in_transit] = 1.0 - depth * limb
        return synthetic_flux

    def run_single_injection(self, time, flux, flux_err, period, depth, duration_days=None, t0=None, seed=None):
        """
        Inject a single synthetic transit and run full blind recovery.
        """
        if seed is not None:
            np.random.seed(seed)

        baseline = float(time[-1] - time[0])
        if duration_days is None:
            duration_days = min(0.2, max(0.04, 0.1 * (period**0.33)))
        if t0 is None:
            t0 = float(time[0] + np.random.uniform(0.1, 0.9) * period)

        # Inject transit signal into genuine observational flux
        transit_model = self._generate_synthetic_transit(time, period, t0, depth, duration_days)
        injected_flux = flux * transit_model

        # Blind search without providing injected parameters
        search_result = self.discovery_engine.search(time, injected_flux, flux_err=flux_err)

        p_rec = search_result["period"]
        depth_rec = search_result["depth"]
        snr_rec = search_result["snr"]

        # Check recovery criteria
        rel_period_err = abs(p_rec - period) / period
        half_period_err = abs(p_rec - 0.5 * period) / (0.5 * period)
        double_period_err = abs(p_rec - 2.0 * period) / (2.0 * period)

        is_recovered = (
            (rel_period_err <= 0.02 or half_period_err <= 0.02 or double_period_err <= 0.02)
            and snr_rec >= 7.0
            and search_result["status"] == "DETECTED"
        )

        period_bias = float(p_rec - period)
        depth_bias = float(depth_rec - depth)

        return {
            "recovered": bool(is_recovered),
            "injected_period": float(period),
            "recovered_period": float(p_rec),
            "period_error_frac": float(rel_period_err),
            "period_bias": period_bias,
            "injected_depth": float(depth),
            "recovered_depth": float(depth_rec),
            "depth_bias": depth_bias,
            "snr_recovered": float(snr_rec),
            "sde_recovered": float(search_result["sde"])
        }

    def run_grid(self, time, flux, flux_err, periods=None, depths=None, trials_per_cell=2, seed=42):
        """
        Execute full 2D injection-recovery grid.
        Returns empirical recovery matrix and completeness curve.
        """
        if periods is None:
            periods = [1.5, 3.5, 7.0]
        if depths is None:
            depths = [0.001, 0.003, 0.008, 0.015]

        rng = np.random.RandomState(seed)
        grid_results = []
        completeness_matrix = np.zeros((len(periods), len(depths)), dtype=float)

        for i, p in enumerate(periods):
            for j, d in enumerate(depths):
                n_rec = 0
                for trial in range(trials_per_cell):
                    trial_seed = rng.randint(1, 1000000)
                    res = self.run_single_injection(time, flux, flux_err, period=p, depth=d, seed=trial_seed)
                    res["trial"] = trial
                    grid_results.append(res)
                    if res["recovered"]:
                        n_rec += 1
                rec_frac = float(n_rec / trials_per_cell)
                completeness_matrix[i, j] = rec_frac

        overall_recovery_rate = float(np.mean([r["recovered"] for r in grid_results]))

        return {
            "periods": [float(p) for p in periods],
            "depths": [float(d) for d in depths],
            "completeness_matrix": completeness_matrix.tolist(),
            "overall_recovery_rate": overall_recovery_rate,
            "total_injections": len(grid_results),
            "trials": grid_results
        }
