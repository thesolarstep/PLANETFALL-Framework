import pytest
import numpy as np
from planetfall.engines.detrending import biweight_detrend, median_detrend, spline_detrend

def test_biweight_detrending_preserves_transit():
    """Verify biweight detrending removes low-frequency trend while preserving transit dip."""
    time = np.linspace(0, 10, 2000)
    # Slow stellar trend: parabolic drift
    trend_true = 1.0 + 0.01 * np.sin(time / 2.0)
    # Transit at t=5.0 with 1% depth
    transit = np.zeros_like(time)
    transit[np.abs(time - 5.0) < 0.05] = 0.01
    
    flux_raw = (trend_true - transit)
    det_flux, trend_est = biweight_detrend(time, flux_raw, window_length=1.0)

    # In transit dip should be preserved at ~0.99
    in_tr = np.abs(time - 5.0) < 0.03
    assert np.mean(det_flux[in_tr]) < 0.992
    # Out of transit continuum should be normalized to ~1.0
    out_tr = np.abs(time - 5.0) > 0.2
    assert abs(np.mean(det_flux[out_tr]) - 1.0) < 0.002
