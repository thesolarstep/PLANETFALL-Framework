import numpy as np
from scipy.interpolate import UnivariateSpline

def biweight_location(arr, c=4.685):
    """Compute Tukey's biweight robust location estimator."""
    arr = arr[np.isfinite(arr)]
    if len(arr) == 0:
        return np.nan
    if len(arr) <= 2:
        return np.median(arr)
    
    med = np.median(arr)
    mad = np.median(np.abs(arr - med))
    if mad == 0:
        return med
    
    u = (arr - med) / (c * 1.4826 * mad)
    mask = np.abs(u) < 1.0
    if not np.any(mask):
        return med
        
    weights = (1.0 - u[mask]**2)**2
    return np.sum(weights * arr[mask]) / np.sum(weights)

def biweight_detrend(time, flux, window_length=0.5, step_size=None):
    """
    Robust running biweight filter for stellar variability removal.
    
    Parameters:
    -----------
    time : np.ndarray
        Timestamps
    flux : np.ndarray
        Normalized flux
    window_length : float
        Filter window duration in days (default 0.5 d = 12 hr)
    step_size : float, optional
        Sampling interval for trend evaluation in days (defaults to window_length / 4)
    """
    time = np.asarray(time)
    flux = np.asarray(flux)
    
    if step_size is None:
        step_size = window_length / 4.0

    eval_times = np.arange(time[0], time[-1] + step_size, step_size)
    trend_vals = []

    half_win = window_length / 2.0
    for t_eval in eval_times:
        in_win = (time >= t_eval - half_win) & (time <= t_eval + half_win)
        if np.sum(in_win) >= 5:
            trend_vals.append(biweight_location(flux[in_win]))
        elif np.sum(in_win) > 0:
            trend_vals.append(np.median(flux[in_win]))
        else:
            trend_vals.append(np.nan)

    trend_vals = np.array(trend_vals)
    valid = np.isfinite(trend_vals)
    if np.sum(valid) < 2:
        trend = np.ones_like(flux)
    else:
        trend = np.interp(time, eval_times[valid], trend_vals[valid])

    detrended_flux = flux / trend
    return detrended_flux, trend

def median_detrend(time, flux, window_length=0.5, step_size=None):
    """Running median detrending."""
    time = np.asarray(time)
    flux = np.asarray(flux)
    if step_size is None:
        step_size = window_length / 4.0

    eval_times = np.arange(time[0], time[-1] + step_size, step_size)
    trend_vals = []
    half_win = window_length / 2.0
    for t_eval in eval_times:
        in_win = (time >= t_eval - half_win) & (time <= t_eval + half_win)
        if np.sum(in_win) > 0:
            trend_vals.append(np.median(flux[in_win]))
        else:
            trend_vals.append(np.nan)

    trend_vals = np.array(trend_vals)
    valid = np.isfinite(trend_vals)
    if np.sum(valid) < 2:
        trend = np.ones_like(flux)
    else:
        trend = np.interp(time, eval_times[valid], trend_vals[valid])

    detrended_flux = flux / trend
    return detrended_flux, trend

def spline_detrend(time, flux, knot_spacing=0.75):
    """Iteratively clipped cubic spline detrending."""
    time = np.asarray(time)
    flux = np.asarray(flux)
    
    n_knots = max(3, int((time[-1] - time[0]) / knot_spacing))
    s = len(time) * 0.001
    
    # Clip out apparent transits before fitting spline so spline doesn't dive into transits
    med = np.median(flux)
    mad = np.median(np.abs(flux - med))
    mask = flux >= (med - 2.5 * 1.4826 * mad)
    
    if np.sum(mask) < 20:
        mask = np.ones_like(flux, dtype=bool)
        
    try:
        spl = UnivariateSpline(time[mask], flux[mask], s=s, k=3)
        trend = spl(time)
        # Avoid unphysical negative or zero trend
        trend[trend <= 0] = 1.0
    except Exception:
        trend = np.ones_like(flux)
        
    detrended_flux = flux / trend
    return detrended_flux, trend
