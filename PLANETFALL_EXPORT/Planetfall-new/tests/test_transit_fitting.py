import pytest
import numpy as np
from planetfall.engines.transit_fitter import TransitModelFitter

def test_mandel_agol_transit_fitting_known_signal():
    """Verify Mandel-Agol fitting recovers known injected transit parameters."""
    time = np.linspace(0, 10, 2000)
    true_period = 2.5
    true_t0 = 1.0
    true_rp = 0.10  # true depth = 0.0100 (1%)
    true_a_rs = 12.0
    true_inc = 88.5
    
    fitter = TransitModelFitter(u1=0.3, u2=0.2)
    synthetic_flux = fitter._eval_model(time, true_period, true_t0, true_rp, true_a_rs, true_inc, 0.3, 0.2)
    # Add slight Gaussian noise
    noise = np.random.normal(0, 0.0002, len(time))
    flux = synthetic_flux + noise
    flux_err = np.ones_like(flux) * 0.0002

    res = fitter.fit(time, flux, flux_err, true_period, true_t0, initial_depth=0.01, initial_duration_days=0.1)

    assert abs(res["rp_rs"] - true_rp) / true_rp < 0.05, f"Rp/Rs error too large: {res['rp_rs']} vs {true_rp}"
    assert abs(res["depth"] - (true_rp**2)) / (true_rp**2) < 0.10, f"Depth error too large: {res['depth']}"
    assert res["delta_bic"] > 10.0, "Delta BIC should strongly favor transit over flat line"
    assert res["reduced_chi2"] < 2.0, f"Reduced chi2 unphysical: {res['reduced_chi2']}"
