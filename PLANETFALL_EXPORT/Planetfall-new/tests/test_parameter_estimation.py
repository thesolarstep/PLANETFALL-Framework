import pytest
from planetfall.engines.parameter_estimation import ParameterEstimation

def test_physical_parameter_derivation():
    """Verify Keplerian physics and insolation derivation for hot Jupiter."""
    # Hot Jupiter around solar-type star: P = 1.0 day, Rp/Rs = 0.10
    res = ParameterEstimation.estimate(
        rp_rs=0.10, rp_rs_err=0.002,
        period_days=1.0,
        r_star=1.0, r_star_err=0.03,
        m_star=1.0, m_star_err=0.05,
        teff_star=5777.0, teff_star_err=80.0
    )

    # a should be ~0.0196 AU
    assert 0.018 < res["semi_major_axis_au"] < 0.022
    # Radius in Jupiter radii should be ~0.97 R_jup
    assert 0.90 < res["planet_radius_jup"] < 1.05
    # Radius in Earth radii should be ~10.9 R_earth
    assert 10.0 < res["planet_radius_earth"] < 12.0
    # Teq should be hot (> 1500 K)
    assert res["equilibrium_temp_k"] > 1400.0
    assert "Too Hot" in res["habitable_zone_status"]
    assert res["physical_regime"] == "Jovian / Gas Giant"
