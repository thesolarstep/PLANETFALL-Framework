import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def generate_diagnostic_plots(time, flux, flux_err, period, t0, duration_days,
                              discovery_res, fit_res, oddeven_res, secondary_res,
                              out_filepath, target_name="Candidate"):
    """
    Generate authentic 5-panel scientific diagnostic plot from real photometry and models.
    Zero fake lines or mocked noise.
    """
    fig, axes = plt.subplots(3, 2, figsize=(16, 12))
    fig.suptitle(f"PLANETFALL Validation Diagnostics: {target_name} (P = {period:.4f} d)", fontsize=16, fontweight="bold")

    # Panel 1: Full Detrended Light Curve
    ax1 = axes[0, 0]
    ax1.plot(time, flux, 'k.', markersize=2, alpha=0.4, label="Photometry")
    
    # Mark transit windows
    transit_epochs = discovery_res.get("transit_epochs", [])
    half_dur = 0.5 * duration_days
    for te in transit_epochs:
        ax1.axvspan(te - half_dur, te + half_dur, color='red', alpha=0.15)
        
    ax1.set_xlabel("Time (BJD / BTJD)")
    ax1.set_ylabel("Normalized Flux")
    ax1.set_title("Detrended Light Curve (Transits Highlighted)")
    ax1.grid(True, alpha=0.3)

    # Panel 2: BLS Periodogram
    ax2 = axes[0, 1]
    periods = discovery_res.get("periods_grid")
    power = discovery_res.get("power_grid")
    if periods is not None and power is not None:
        ax2.plot(periods, power, 'b-', lw=1.2, label="BLS Power")
        ax2.axvline(period, color='r', linestyle='--', label=f"Peak P = {period:.4f} d")
        ax2.axvline(period / 2.0, color='orange', linestyle=':', label="P / 2")
        ax2.axvline(period * 2.0, color='purple', linestyle=':', label="2P")
        ax2.set_xlabel("Period (days)")
        ax2.set_ylabel("BLS Power")
        ax2.set_title(f"Transit Periodogram (SDE = {discovery_res.get('sde', 0):.1f})")
        ax2.legend(loc="upper right", fontsize=8)
        ax2.grid(True, alpha=0.3)
    else:
        ax2.text(0.5, 0.5, "Periodogram data unavailable", ha="center", va="center")

    # Panel 3: Phased Light Curve with Fitted Mandel-Agol Model
    ax3 = axes[1, 0]
    phase = ((time - t0 + 0.5 * period) % period) / period - 0.5
    phase_hours = phase * period * 24.0
    
    # Sort for model line
    sort_idx = np.argsort(phase_hours)
    ph_sorted = phase_hours[sort_idx]
    f_sorted = flux[sort_idx]

    # Zoom window: 4 transit durations
    win_hours = 2.0 * duration_days * 24.0
    zoom_mask = np.abs(ph_sorted) <= win_hours
    
    ax3.plot(ph_sorted[zoom_mask], f_sorted[zoom_mask], 'k.', markersize=3, alpha=0.3, label="Data")
    
    # Binned points
    bins = np.linspace(-win_hours, win_hours, 40)
    bin_centers = 0.5 * (bins[1:] + bins[:-1])
    bin_means = []
    bin_errs = []
    for b0, b1 in zip(bins[:-1], bins[1:]):
        in_bin = (ph_sorted >= b0) & (ph_sorted < b1)
        if np.sum(in_bin) > 0:
            bin_means.append(np.median(f_sorted[in_bin]))
            bin_errs.append(np.std(f_sorted[in_bin]) / np.sqrt(np.sum(in_bin)))
        else:
            bin_means.append(np.nan)
            bin_errs.append(np.nan)
            
    ax3.errorbar(bin_centers, bin_means, yerr=bin_errs, fmt='ro', markersize=4, label="Binned (40 bins)")

    # Model curve
    model_flux = fit_res.get("model_flux")
    if model_flux is not None:
        m_sorted = model_flux[sort_idx]
        ax3.plot(ph_sorted[zoom_mask], m_sorted[zoom_mask], 'b-', lw=2.0, label="Mandel-Agol Fit")
        
    ax3.set_xlabel("Time from Mid-Transit (Hours)")
    ax3.set_ylabel("Normalized Flux")
    ax3.set_title(f"Phased Transit Model Fit (Depth = {fit_res.get('depth', 0)*1e6:.0f} ppm)")
    ax3.legend(loc="lower right", fontsize=8)
    ax3.grid(True, alpha=0.3)

    # Panel 4: Fit Residuals
    ax4 = axes[1, 1]
    resids = fit_res.get("residuals")
    if resids is not None:
        r_sorted = resids[sort_idx]
        ax4.plot(ph_sorted[zoom_mask], r_sorted[zoom_mask], 'k.', markersize=3, alpha=0.4)
        ax4.axhline(0, color='r', linestyle='--')
        ax4.set_xlabel("Time from Mid-Transit (Hours)")
        ax4.set_ylabel("Residuals (Data - Model)")
        ax4.set_title(f"Fit Residuals (RMS = {fit_res.get('residual_rms', 0)*1e6:.1f} ppm)")
        ax4.grid(True, alpha=0.3)
    else:
        ax4.text(0.5, 0.5, "Residuals unavailable", ha="center", va="center")

    # Panel 5: Odd vs Even Transits
    ax5 = axes[2, 0]
    epoch_float = (time - t0) / period
    epoch_int = np.round(epoch_float).astype(int)
    odd = (epoch_int % 2 != 0)
    even = (epoch_int % 2 == 0)

    ax5.plot(phase_hours[odd & (np.abs(phase_hours) <= win_hours)], flux[odd & (np.abs(phase_hours) <= win_hours)], 'b.', markersize=3, alpha=0.4, label=f"Odd (Depth: {oddeven_res.get('depth_odd', 0)*1e6:.0f} ppm)")
    ax5.plot(phase_hours[even & (np.abs(phase_hours) <= win_hours)], flux[even & (np.abs(phase_hours) <= win_hours)], 'r.', markersize=3, alpha=0.4, label=f"Even (Depth: {oddeven_res.get('depth_even', 0)*1e6:.0f} ppm)")
    ax5.set_xlabel("Time from Transit (Hours)")
    ax5.set_ylabel("Normalized Flux")
    ax5.set_title(f"Odd-Even Check (Z = {oddeven_res.get('z_score', 0):.2f}, Verdict: {oddeven_res.get('status', 'N/A')})")
    ax5.legend(loc="lower right", fontsize=8)
    ax5.grid(True, alpha=0.3)

    # Panel 6: Secondary Eclipse Zoom (Phase ~ 0.5)
    ax6 = axes[2, 1]
    phase_sec_hours = (((phase + 1.0) % 1.0) - 0.5) * period * 24.0
    sec_zoom = np.abs(np.abs(phase_sec_hours) - (0.5 * period * 24.0)) <= win_hours
    
    # Fold around secondary center (0.5 P)
    sec_offset_hours = np.abs(phase_hours) - (0.5 * period * 24.0)
    sec_mask = np.abs(sec_offset_hours) <= win_hours
    
    ax6.plot(sec_offset_hours[sec_mask], flux[sec_mask], 'k.', markersize=3, alpha=0.3, label="Data")
    ax6.axhline(1.0, color='r', linestyle='--')
    ax6.set_xlabel("Time from Secondary Center (Hours)")
    ax6.set_ylabel("Normalized Flux")
    ax6.set_title(f"Secondary Eclipse Search (SNR = {secondary_res.get('secondary_snr', 0):.2f}, Verdict: {secondary_res.get('status', 'N/A')})")
    ax6.grid(True, alpha=0.3)

    plt.tight_layout()
    os.makedirs(os.path.dirname(os.path.abspath(out_filepath)), exist_ok=True)
    fig.savefig(out_filepath, dpi=150)
    plt.close(fig)
    return out_filepath
