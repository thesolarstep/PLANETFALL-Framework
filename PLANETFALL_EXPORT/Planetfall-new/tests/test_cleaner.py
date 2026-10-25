import pytest
import numpy as np
from planetfall.data.cleaner import LightCurveCleaner

def test_lightcurve_cleaner():
    """Verify cleaner strips NaNs, normalizes flux, and calculates noise metrics."""
    time = np.linspace(1.0, 10.0, 30)
    flux = 1000.0 + np.random.normal(0, 1.0, 30)
    # Inject some NaNs
    time[5] = np.nan
    flux[10] = np.nan
    
    cleaned = LightCurveCleaner.clean(time, flux)
    
    assert len(cleaned["time"]) == 28
    assert not np.any(np.isnan(cleaned["time"]))
    assert not np.any(np.isnan(cleaned["flux"]))
    # Median normalized to ~1.0
    assert abs(np.median(cleaned["flux"]) - 1.0) < 0.01
    assert cleaned["cdpp_est_ppm"] > 0.0
