import numpy as np

class OddEvenValidator:
    """
    Performs independent odd-even transit depth difference test.
    Distinguishes planetary transits from eclipsing binaries (EBs) whose true orbital period is 2P.
    Zero ground-truth label leakage.
    """

    @staticmethod
    def test(time, flux, flux_err, period, t0, duration_days):
        """
        Evaluate statistical significance of odd vs even transit depths.
        """
        time = np.asarray(time)
        flux = np.asarray(flux)
        flux_err = np.asarray(flux_err) if flux_err is not None else np.ones_like(flux) * 0.001

        # Calculate epoch number for each observation point
        epoch_float = (time - t0) / period
        epoch_int = np.round(epoch_float).astype(int)

        # Distance from nearest transit center in days
        dt_center = np.abs(time - (t0 + epoch_int * period))
        half_dur = 0.5 * duration_days

        in_transit = dt_center < half_dur
        out_transit = (dt_center >= (1.5 * half_dur)) & (dt_center <= (3.5 * half_dur))

        odd_epochs = (epoch_int % 2 != 0)
        even_epochs = (epoch_int % 2 == 0)

        in_odd = in_transit & odd_epochs
        in_even = in_transit & even_epochs
        out_odd = out_transit & odd_epochs
        out_even = out_transit & even_epochs

        n_odd = int(np.sum(in_odd))
        n_even = int(np.sum(in_even))

        if n_odd < 3 or n_even < 3:
            return {
                "status": "UNRESOLVED",
                "reason": "Insufficient transits in odd or even phase",
                "z_score": 0.0,
                "p_value": 1.0,
                "depth_odd": 0.0,
                "depth_even": 0.0,
                "depth_difference": 0.0
            }

        # Measure baseline and transit depth for odd transits
        base_odd = np.nanmedian(flux[out_odd]) if np.sum(out_odd) > 0 else 1.0
        depth_odd = float(base_odd - np.nanmedian(flux[in_odd]))
        mad_odd = float(np.nanmedian(np.abs(flux[in_odd] - np.nanmedian(flux[in_odd]))) * 1.4826)
        sigma_odd = max(1e-5, mad_odd / np.sqrt(n_odd))

        # Measure baseline and transit depth for even transits
        base_even = np.nanmedian(flux[out_even]) if np.sum(out_even) > 0 else 1.0
        depth_even = float(base_even - np.nanmedian(flux[in_even]))
        mad_even = float(np.nanmedian(np.abs(flux[in_even] - np.nanmedian(flux[in_even]))) * 1.4826)
        sigma_even = max(1e-5, mad_even / np.sqrt(n_even))

        # Depth difference and z-score
        delta_depth = abs(depth_odd - depth_even)
        combined_sigma = np.sqrt(sigma_odd**2 + sigma_even**2)
        z_score = float(delta_depth / combined_sigma)

        # Standard normal two-tailed p-value approximation
        from scipy.stats import norm
        p_val = float(2.0 * (1.0 - norm.cdf(z_score)))

        # If z_score > 3.0 (p < 0.0027), reject candidate as likely eclipsing binary
        is_eb = z_score >= 3.0
        status = "REJECTED_ECLIPSING_BINARY" if is_eb else "PASSED"

        return {
            "status": status,
            "z_score": z_score,
            "p_value": p_val,
            "depth_odd": depth_odd,
            "depth_odd_err": sigma_odd,
            "depth_even": depth_even,
            "depth_even_err": sigma_even,
            "depth_difference": delta_depth,
            "depth_difference_err": float(combined_sigma),
            "n_odd_points": n_odd,
            "n_even_points": n_even
        }

def test_oddeven(time, flux, flux_err, period, t0, duration_days):
    return OddEvenValidator.test(time, flux, flux_err, period, t0, duration_days)
