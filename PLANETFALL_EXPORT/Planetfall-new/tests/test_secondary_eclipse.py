import pytest
import numpy as np
from planetfall.validators.secondary_eclipse import SecondaryEclipseValidator

def test_secondary_eclipse_detection():
    """Verify secondary eclipse validator detects thermal/reflected secondary eclipse."""
    time = np.linspace(0, 20, 4000)
    period = 2.0
    t0 = 0.5
    dur = 0.10

    flux = np.ones_like(time)
    epoch_float = (time - t0) / period
    epoch_int = np.round(epoch_float).astype(int)
    
    # Primary transit at phase 0
    dt_pri = np.abs(time - (t0 + epoch_int * period))
    flux[dt_pri < (0.5 * dur)] -= 0.020

    # Secondary eclipse at phase 0.5
    dt_sec = np.abs(time - (t0 + (epoch_int + 0.5) * period))
    flux[dt_sec < (0.5 * dur)] -= 0.005

    flux += np.random.normal(0, 0.0003, len(time))
    flux_err = np.ones_like(flux) * 0.0003

    res = SecondaryEclipseValidator.test(time, flux, flux_err, period, t0, dur, primary_depth=0.020)

    assert res["status"] == "REJECTED_SECONDARY_ECLIPSE"
    assert res["secondary_snr"] >= 3.0
    assert res["secondary_depth"] > 0.002

def test_no_secondary_eclipse_planet():
    """Verify clean planet light curve passes secondary eclipse check."""
    time = np.linspace(0, 20, 4000)
    period = 2.0
    t0 = 0.5
    dur = 0.10

    flux = np.ones_like(time)
    epoch_float = (time - t0) / period
    epoch_int = np.round(epoch_float).astype(int)
    dt_pri = np.abs(time - (t0 + epoch_int * period))
    flux[dt_pri < (0.5 * dur)] -= 0.010
    flux += np.random.normal(0, 0.0003, len(time))
    flux_err = np.ones_like(flux) * 0.0003

    res = SecondaryEclipseValidator.test(time, flux, flux_err, period, t0, dur, primary_depth=0.010)

    assert res["status"] == "PASSED"
    assert res["secondary_snr"] < 3.0
