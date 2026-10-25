import numpy as np

class CentroidValidator:
    """
    Analyzes pixel-level Target Pixel Files (TPF) to detect photocenter centroid shifts.
    Distinguishes on-target transits from nearby contaminating background eclipsing binaries (NEBs).
    If TPF is unavailable, reports UNAVAILABLE / NOT_TESTED honestly.
    """

    @staticmethod
    def test(tpf, period, t0, duration_days):
        """
        Evaluate pixel centroid shift during transit.
        
        Parameters:
        -----------
        tpf : lightkurve.TargetPixelFile or None
        period : float
        t0 : float
        duration_days : float
        """
        if tpf is None:
            return {
                "status": "NOT_TESTED",
                "reason": "Target Pixel File (TPF) unavailable for target",
                "centroid_shift_pixels": None,
                "centroid_shift_arcsec": None,
                "sigma_offset": None
            }

        try:
            time = tpf.time.value
            flux = tpf.flux.value  # Shape: (n_cadences, nrows, ncols)

            if flux is None or len(flux.shape) != 3:
                return {
                    "status": "NOT_TESTED",
                    "reason": "Malformed TPF flux cube",
                    "centroid_shift_pixels": None,
                    "centroid_shift_arcsec": None
                }

            # Phase and find in-transit cadences
            phase = ((time - t0 + 0.5 * period) % period) / period - 0.5
            phase_days = np.abs(phase * period)
            half_dur = 0.5 * duration_days

            in_transit = phase_days < half_dur
            out_transit = (phase_days >= (1.5 * half_dur)) & (phase_days <= (3.5 * half_dur))

            if np.sum(in_transit) < 3 or np.sum(out_transit) < 5:
                return {
                    "status": "UNRESOLVED",
                    "reason": "Insufficient valid TPF frames in-transit or baseline",
                    "centroid_shift_pixels": None,
                    "centroid_shift_arcsec": None
                }

            # Mean images
            img_in = np.nanmean(flux[in_transit], axis=0)
            img_out = np.nanmean(flux[out_transit], axis=0)
            img_diff = img_out - img_in

            # Replace any NaNs
            img_out = np.nan_to_num(img_out, nan=0.0)
            img_diff = np.nan_to_num(img_diff, nan=0.0)
            # Clip negative difference pixels
            img_diff[img_diff < 0] = 0.0

            # Compute centroids: sum(x * I) / sum(I)
            nrows, ncols = img_out.shape
            yy, xx = np.mgrid[0:nrows, 0:ncols]

            sum_out = np.sum(img_out)
            sum_diff = np.sum(img_diff)

            if sum_out <= 0 or sum_diff <= 0:
                return {
                    "status": "UNRESOLVED",
                    "reason": "Difference image flux non-positive",
                    "centroid_shift_pixels": None,
                    "centroid_shift_arcsec": None
                }

            x_out = np.sum(xx * img_out) / sum_out
            y_out = np.sum(yy * img_out) / sum_out

            x_diff = np.sum(xx * img_diff) / sum_diff
            y_diff = np.sum(yy * img_diff) / sum_diff

            # Pixel offset
            dr_pix = float(np.sqrt((x_diff - x_out)**2 + (y_diff - y_out)**2))
            # TESS pixel scale is 21 arcsec / pixel
            dr_arcsec = float(dr_pix * 21.0)

            # Standard threshold: > 1.0 pixel offset indicates off-target source
            is_offset = dr_pix > 1.0
            status = "REJECTED_CENTROID_OFFSET" if is_offset else "PASSED"

            return {
                "status": status,
                "centroid_shift_pixels": dr_pix,
                "centroid_shift_arcsec": dr_arcsec,
                "target_centroid": (float(x_out), float(y_out)),
                "difference_centroid": (float(x_diff), float(y_diff)),
                "in_transit_frames": int(np.sum(in_transit)),
                "out_transit_frames": int(np.sum(out_transit))
            }

        except Exception as e:
            return {
                "status": "ERROR",
                "reason": f"Centroid analysis failed: {e}",
                "centroid_shift_pixels": None,
                "centroid_shift_arcsec": None
            }

def test_centroid(tpf, period, t0, duration_days):
    return CentroidValidator.test(tpf, period, t0, duration_days)
