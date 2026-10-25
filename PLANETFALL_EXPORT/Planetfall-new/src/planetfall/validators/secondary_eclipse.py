import numpy as np

class SecondaryEclipseValidator:
    """
    Constrains and detects secondary eclipses in phased photometry.
    Distinguishes self-luminous or thermal stellar companions from transiting planets.
    Zero canned text.
    """

    @staticmethod
    def test(time, flux, flux_err, period, t0, duration_days, primary_depth):
        """
        Search for secondary eclipse near phase 0.5.
        """
        time = np.asarray(time)
        flux = np.asarray(flux)
        flux_err = np.asarray(flux_err) if flux_err is not None else np.ones_like(flux) * 0.001

        # Phase from -0.5 to +0.5 where 0 is primary transit
        phase = ((time - t0 + 0.5 * period) % period) / period - 0.5
        dur_phase = duration_days / period

        # Secondary eclipse window (circular orbit expectation: phase = +0.5 or -0.5)
        # Distance from phase +/-0.5:
        dist_to_sec = np.abs(np.abs(phase) - 0.5)

        half_dur_phase = 0.5 * dur_phase
        in_secondary = dist_to_sec <= half_dur_phase
        # Out of secondary baseline in phase range away from both primary (phase 0) and secondary (phase 0.5)
        # e.g., phase distance from secondary between 1.5 and 3.5 half durations, and away from primary
        dist_to_pri = np.abs(phase)
        out_secondary = (dist_to_sec > (1.5 * half_dur_phase)) & (dist_to_sec <= (4.0 * half_dur_phase)) & (dist_to_pri > (2.0 * half_dur_phase))

        n_sec = int(np.sum(in_secondary))
        n_base = int(np.sum(out_secondary))

        if n_sec < 5:
            return {
                "status": "UNRESOLVED",
                "reason": "Insufficient photometric points in secondary eclipse window",
                "secondary_depth": 0.0,
                "secondary_depth_err": 0.0,
                "secondary_snr": 0.0,
                "upper_limit_3sigma": 0.0
            }

        base_flux = np.nanmedian(flux[out_secondary]) if n_base > 0 else 1.0
        sec_flux = np.nanmedian(flux[in_secondary])
        sec_depth = float(base_flux - sec_flux)

        mad = float(np.nanmedian(np.abs(flux[out_secondary] - base_flux)) * 1.4826) if n_base > 0 else 1e-4
        sec_err = max(1e-5, mad / np.sqrt(n_sec))

        sec_snr = float(sec_depth / sec_err)
        upper_limit_3sigma = float(max(0.0, sec_depth) + 3.0 * sec_err)

        # Flag as false positive if secondary eclipse is detected with SNR >= 3.0
        # and has depth > 5% of primary transit depth
        is_detected = (sec_snr >= 3.0) and (sec_depth >= 0.05 * primary_depth) and (sec_depth > 0.0002)

        status = "REJECTED_SECONDARY_ECLIPSE" if is_detected else "PASSED"

        return {
            "status": status,
            "secondary_depth": sec_depth,
            "secondary_depth_err": sec_err,
            "secondary_snr": sec_snr,
            "upper_limit_3sigma": upper_limit_3sigma,
            "depth_ratio_to_primary": float(sec_depth / max(1e-6, primary_depth)),
            "points_in_secondary": n_sec
        }

def test_secondary_eclipse(time, flux, flux_err, period, t0, duration_days, primary_depth):
    return SecondaryEclipseValidator.test(time, flux, flux_err, period, t0, duration_days, primary_depth)
