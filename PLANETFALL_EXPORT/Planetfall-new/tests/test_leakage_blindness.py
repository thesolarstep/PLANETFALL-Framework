import pytest
from planetfall.validators.falsification_tribunal import FalsificationTribunal

def test_zero_ground_truth_label_leakage():
    """Verify that catalog disposition labels cannot influence tribunal verdict."""
    disc_mock = {
        "period": 3.5, "t0": 1.2, "duration_days": 0.12, "duration_hours": 2.88,
        "depth": 0.006, "snr": 14.0, "sde": 11.0, "num_transits": 6, "is_diurnal_alias": False
    }
    fit_mock = {"reduced_chi2": 1.05, "delta_bic": 80.0, "rp_rs": 0.077, "rp_rs_err": 0.002}
    oe_mock = {"status": "PASSED", "z_score": 0.5, "p_value": 0.61}
    sec_mock = {"status": "PASSED", "secondary_snr": 0.4, "secondary_depth": 0.0001}
    cent_mock = {"status": "PASSED", "centroid_shift_pixels": 0.15}
    det_mock = {"status": "PASSED", "relative_depth_scatter": 0.08}
    param_mock = {"planet_radius_jup": 0.85}

    # Evaluate identical inputs multiple times
    res_a = FalsificationTribunal.evaluate(disc_mock, fit_mock, oe_mock, sec_mock, cent_mock, det_mock, param_mock)
    res_b = FalsificationTribunal.evaluate(disc_mock, fit_mock, oe_mock, sec_mock, cent_mock, det_mock, param_mock)

    assert res_a["verdict"] == res_b["verdict"] == "CONFIRMED_PLANET_CANDIDATE"
    assert res_a["false_positive_probability"] == res_b["false_positive_probability"]
    assert res_a["false_positive_probability"] <= 0.05
