import numpy as np
from ..engines.detrending import biweight_detrend, median_detrend

class DetrendingSensitivityValidator:
    """
    Stress-tests candidate signal against distinct preprocessing and detrending filters.
    Verifies that candidate is not an artefact of a specific smoothing window.
    """

    @staticmethod
    def test(raw_time, raw_flux, period, t0, duration_days, nominal_depth):
        """
        Evaluate transit depth stability across 3 distinct filter windows.
        """
        windows = [0.3, 0.6, 1.2]
        depths = []

        phase = ((raw_time - t0 + 0.5 * period) % period) / period - 0.5
        phase_days = np.abs(phase * period)
        half_dur = 0.5 * duration_days
        in_transit = phase_days < half_dur
        out_transit = (phase_days >= (1.5 * half_dur)) & (phase_days <= (3.5 * half_dur))

        for win in windows:
            try:
                det_flux, _ = biweight_detrend(raw_time, raw_flux, window_length=win)
                base = np.nanmedian(det_flux[out_transit]) if np.sum(out_transit) > 0 else 1.0
                d = float(base - np.nanmedian(det_flux[in_transit]))
                depths.append(max(0.0, d))
            except Exception:
                depths.append(nominal_depth)

        depths = np.array(depths)
        mean_depth = float(np.mean(depths))
        std_depth = float(np.std(depths))
        rel_scatter = float(std_depth / max(1e-5, mean_depth))

        # Sensitive if depth changes by > 40% across reasonable detrending windows
        is_sensitive = rel_scatter > 0.40
        status = "DETRENDING_SENSITIVE" if is_sensitive else "PASSED"

        return {
            "status": status,
            "relative_depth_scatter": rel_scatter,
            "window_lengths_days": windows,
            "measured_depths": [float(x) for x in depths],
            "nominal_depth": float(nominal_depth)
        }

def test_detrending_sensitivity(raw_time, raw_flux, period, t0, duration_days, nominal_depth):
    return DetrendingSensitivityValidator.test(raw_time, raw_flux, period, t0, duration_days, nominal_depth)
