import pytest
import numpy as np
from planetfall.validators.oddeven import OddEvenValidator

def test_oddeven_eclipsing_binary_detection():
    """Verify odd-even validator flags eclipsing binary with significant depth mismatch."""
    time = np.linspace(0, 20, 4000)
    period = 2.0
    t0 = 0.5
    dur = 0.10

    flux = np.ones_like(time)
    epoch_float = (time - t0) / period
    epoch_int = np.round(epoch_float).astype(int)
    dt = np.abs(time - (t0 + epoch_int * period))
    in_tr = dt < (0.5 * dur)

    # Primary eclipse: 2% depth; Secondary eclipse: 1% depth
    flux[in_tr & (epoch_int % 2 != 0)] -= 0.020
    flux[in_tr & (epoch_int % 2 == 0)] -= 0.010
    flux += np.random.normal(0, 0.0003, len(time))
    flux_err = np.ones_like(flux) * 0.0003

    res = OddEvenValidator.test(time, flux, flux_err, period, t0, dur)

    assert res["status"] == "REJECTED_ECLIPSING_BINARY"
    assert res["z_score"] >= 3.0
    assert res["p_value"] < 0.005

def test_oddeven_planet_consistency():
    """Verify odd-even validator passes consistent planetary transit signals."""
    time = np.linspace(0, 20, 4000)
    period = 2.0
    t0 = 0.5
    dur = 0.10

    flux = np.ones_like(time)
    epoch_float = (time - t0) / period
    epoch_int = np.round(epoch_float).astype(int)
    dt = np.abs(time - (t0 + epoch_int * period))
    in_tr = dt < (0.5 * dur)

    flux[in_tr] -= 0.015
    flux += np.random.normal(0, 0.0003, len(time))
    flux_err = np.ones_like(flux) * 0.0003

    res = OddEvenValidator.test(time, flux, flux_err, period, t0, dur)

    assert res["status"] == "PASSED"
    assert res["z_score"] < 2.5
