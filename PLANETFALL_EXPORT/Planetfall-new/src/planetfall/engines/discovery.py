import numpy as np
from astropy.timeseries import BoxLeastSquares

class BlindDiscoveryEngine:
    """
    Independent blind transit search engine.
    Ingests time-series photometry without access to known periods, dispositions, or identities.
    """

    def __init__(self, period_min=0.5, period_max=25.0, duration_hours=None, min_snr=5.0):
        self.period_min = period_min
        self.period_max = period_max
        self.duration_hours = duration_hours or [1.0, 1.5, 2.0, 3.0, 4.0, 5.0]
        self.min_snr = min_snr

    def search(self, time, flux, flux_err=None, n_periods=3500):
        """
        Execute Box Least Squares (BLS) transit search.
        
        Returns:
        --------
        dict:
            Candidate parameters (period, t0, duration, depth, sde, snr)
            Periodogram arrays (periods, power)
            Harmonic & alias checks
        """
        time = np.asarray(time)
        flux = np.asarray(flux)
        if flux_err is not None:
            flux_err = np.asarray(flux_err)

        baseline = float(time[-1] - time[0])
        max_p = min(self.period_max, baseline / 2.0)
        if max_p <= self.period_min:
            max_p = baseline * 0.9

        # Convert duration hours to days
        durations = np.array(self.duration_hours) / 24.0
        durations = durations[durations < (self.period_min * 0.2)]
        if len(durations) == 0:
            durations = np.array([0.05, 0.1, 0.15])

        bls = BoxLeastSquares(time, flux, dy=flux_err)
        periods = np.linspace(self.period_min, max_p, n_periods)
        periodogram = bls.power(periods, durations)

        # Identify maximum peak
        best_idx = np.argmax(periodogram.power)
        best_period = float(periodogram.period[best_idx])
        best_duration = float(periodogram.duration[best_idx])
        best_t0 = float(periodogram.transit_time[best_idx])
        best_depth = float(periodogram.depth[best_idx])
        max_power = float(periodogram.power[best_idx])

        # Compute Signal Detection Efficiency (SDE)
        p_mean = np.nanmean(periodogram.power)
        p_std = np.nanstd(periodogram.power)
        sde = float((max_power - p_mean) / p_std) if p_std > 0 else 0.0

        # Transit SNR calculation
        phase = ((time - best_t0 + 0.5 * best_period) % best_period) / best_period - 0.5
        in_transit = np.abs(phase * best_period) < (0.5 * best_duration)
        n_in = int(np.sum(in_transit))
        n_out = int(np.sum(~in_transit))

        mad_noise = float(np.nanmedian(np.abs(flux[~in_transit] - np.nanmedian(flux[~in_transit]))) * 1.4826) if n_out > 0 else 1e-4
        if mad_noise <= 0:
            mad_noise = 1e-4

        transit_snr = float((best_depth / mad_noise) * np.sqrt(max(1, n_in)))

        # Count individual observed transits
        transit_times = []
        cur_t = best_t0
        while cur_t <= time[-1] + 0.5 * best_period:
            if cur_t >= time[0] - 0.5 * best_period:
                # Check if data points exist near cur_t
                has_points = np.any(np.abs(time - cur_t) < (0.6 * best_duration))
                if has_points:
                    transit_times.append(float(cur_t))
            cur_t += best_period

        num_transits = len(transit_times)

        # Alias analysis
        is_diurnal_alias = False
        alias_reason = "None"
        if np.isclose(best_period, 1.0, atol=0.03):
            is_diurnal_alias = True
            alias_reason = "1.0-day terrestrial diurnal sampling alias"
        elif np.isclose(best_period, 0.5, atol=0.015):
            is_diurnal_alias = True
            alias_reason = "0.5-day terrestrial harmonic alias"

        # Check half and double period power
        half_p = best_period / 2.0
        double_p = best_period * 2.0
        half_idx = np.argmin(np.abs(periods - half_p))
        double_idx = np.argmin(np.abs(periods - double_p))
        half_power = float(periodogram.power[half_idx])
        double_power = float(periodogram.power[double_idx]) if double_p <= max_p else 0.0

        is_subharmonic = half_power > (0.85 * max_power)
        is_superharmonic = double_power > (0.85 * max_power)

        status = "DETECTED" if (transit_snr >= self.min_snr and num_transits >= 2 and not is_diurnal_alias) else "REJECTED"

        return {
            "status": status,
            "period": best_period,
            "t0": best_t0,
            "duration_days": best_duration,
            "duration_hours": best_duration * 24.0,
            "depth": best_depth,
            "sde": sde,
            "snr": transit_snr,
            "num_transits": num_transits,
            "transit_epochs": transit_times,
            "is_diurnal_alias": is_diurnal_alias,
            "alias_reason": alias_reason,
            "is_subharmonic": is_subharmonic,
            "is_superharmonic": is_superharmonic,
            "noise_mad": mad_noise,
            "periods_grid": periods,
            "power_grid": periodogram.power,
            "best_index": int(best_idx)
        }

def search_transits(time, flux, flux_err=None, period_min=0.5, period_max=25.0, min_snr=5.0):
    engine = BlindDiscoveryEngine(period_min=period_min, period_max=period_max, min_snr=min_snr)
    return engine.search(time, flux, flux_err=flux_err)
