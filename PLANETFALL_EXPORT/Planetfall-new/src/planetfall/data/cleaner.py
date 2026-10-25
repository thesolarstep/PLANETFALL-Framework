import numpy as np

class LightCurveCleaner:
    """Preprocesses and conditions photometric time series."""

    @staticmethod
    def clean(time, flux, flux_err=None, quality=None, sigma_clip=5.0):
        """
        Clean and condition raw photometric time series.
        
        Parameters:
        -----------
        time : np.ndarray
            Time array (BJD or BTJD)
        flux : np.ndarray
            Raw or normalized flux measurements
        flux_err : np.ndarray, optional
            Photometric measurement uncertainties
        quality : np.ndarray, optional
            TESS/Kepler quality bitmask flags
        sigma_clip : float
            Threshold for outlier rejection on positive side (preserves negative dips)

        Returns:
        --------
        dict:
            Cleaned arrays: time, flux, flux_err
            Metrics: median_flux, rms_scatter, n_points, gaps
        """
        time = np.asarray(time, dtype=float)
        flux = np.asarray(flux, dtype=float)
        if flux_err is not None:
            flux_err = np.asarray(flux_err, dtype=float)
        else:
            mad_diff = np.nanmedian(np.abs(np.diff(flux))) / 1.4826
            if not np.isfinite(mad_diff) or mad_diff <= 0:
                mad_diff = np.nanstd(flux)
                if not np.isfinite(mad_diff) or mad_diff <= 0:
                    mad_diff = 1e-4
            flux_err = np.ones_like(flux) * max(1e-5, float(mad_diff))

        # 1. Mask non-finite values
        finite_mask = np.isfinite(time) & np.isfinite(flux) & (flux > 0)
        if flux_err is not None:
            finite_mask &= np.isfinite(flux_err) & (flux_err >= 0)

        # 2. Quality mask if available (TESS standard quality flag filter)
        if quality is not None:
            quality = np.asarray(quality, dtype=int)
            # Standard TESS bitmask: exclude bits 1, 2, 3, 4, 5, 6, 8, 10, 12
            bad_bits = 1 | 2 | 4 | 8 | 16 | 32 | 128 | 512 | 2048
            quality_mask = (quality & bad_bits) == 0
            finite_mask &= quality_mask

        t_clean = time[finite_mask]
        f_clean = flux[finite_mask]
        err_clean = flux_err[finite_mask]

        if len(t_clean) < 10:
            raise ValueError(f"Insufficient valid photometric points remaining after filtering: {len(t_clean)}")

        # Sort chronologically
        sort_idx = np.argsort(t_clean)
        t_clean = t_clean[sort_idx]
        f_clean = f_clean[sort_idx]
        err_clean = err_clean[sort_idx]

        # 3. Median normalization
        med_f = np.nanmedian(f_clean)
        if med_f > 0:
            f_clean = f_clean / med_f
            err_clean = err_clean / med_f

        # 4. Asymmetric sigma-clipping: clip extreme positive flares (>sigma_clip * MAD)
        # We do NOT clip negative excursions so we preserve genuine transit dips!
        mad = np.nanmedian(np.abs(f_clean - 1.0))
        std_est = 1.4826 * mad
        if std_est == 0:
            std_est = np.nanstd(f_clean) or 1e-4

        non_flare_mask = (f_clean - 1.0) < (sigma_clip * std_est)
        t_clean = t_clean[non_flare_mask]
        f_clean = f_clean[non_flare_mask]
        err_clean = err_clean[non_flare_mask]

        # 5. Gap detection (> 0.5 days)
        time_diffs = np.diff(t_clean)
        gap_indices = np.where(time_diffs > 0.5)[0]
        gaps = [(float(t_clean[i]), float(t_clean[i+1])) for i in gap_indices]

        # 6. Noise metrics
        rms = float(np.nanstd(f_clean))
        cdpp_ppm = float(std_est * 1e6)

        return {
            "time": t_clean,
            "flux": f_clean,
            "flux_err": err_clean,
            "median_flux": float(med_f),
            "rms_scatter": rms,
            "cdpp_est_ppm": cdpp_ppm,
            "total_points": len(t_clean),
            "gaps": gaps,
            "baseline_days": float(t_clean[-1] - t_clean[0]) if len(t_clean) > 0 else 0.0
        }

def clean_lightcurve(time, flux, flux_err=None, quality=None, sigma_clip=5.0):
    return LightCurveCleaner.clean(time, flux, flux_err, quality, sigma_clip)
