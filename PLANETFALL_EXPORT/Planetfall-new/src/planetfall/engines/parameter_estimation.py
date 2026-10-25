import numpy as np

# Physical constants in SI and astronomical units
R_SUN_TO_R_EARTH = 109.076
R_SUN_TO_R_JUP = 9.73116
AU_IN_METERS = 1.495978707e11
M_SUN_IN_KG = 1.98847e30
R_SUN_IN_METERS = 6.957e8
G_CONST = 6.67430e-11

class ParameterEstimation:
    """
    Computes physical planetary parameters and habitable zone metrics from
    transit observables and stellar host characteristics.
    Zero candidate-specific hardcoding.
    """

    @staticmethod
    def estimate(rp_rs, rp_rs_err, period_days, r_star=1.0, r_star_err=0.05,
                 m_star=1.0, m_star_err=0.08, teff_star=5777.0, teff_star_err=100.0):
        """
        Derive physical characteristics with full analytical error propagation.
        """
        rp_rs = float(rp_rs)
        rp_rs_err = float(rp_rs_err)
        period_days = float(period_days)
        r_star = float(r_star)
        r_star_err = float(r_star_err)
        m_star = float(m_star)
        m_star_err = float(m_star_err)
        teff_star = float(teff_star)
        teff_star_err = float(teff_star_err)

        # 1. Planet Radius (Earth radii & Jupiter radii)
        rp_earth = rp_rs * r_star * R_SUN_TO_R_EARTH
        # Fractional error: (drp/rp)^2 = (dk/k)^2 + (dr*/r*)^2
        rel_err_rp = np.sqrt((rp_rs_err / max(1e-6, rp_rs))**2 + (r_star_err / max(1e-6, r_star))**2)
        rp_earth_err = rp_earth * rel_err_rp
        rp_jup = rp_rs * r_star * R_SUN_TO_R_JUP
        rp_jup_err = rp_jup * rel_err_rp

        # 2. Semi-major axis via Kepler's 3rd Law: a = [G M (P)^2 / (4 pi^2)]^(1/3)
        p_sec = period_days * 86400.0
        m_kg = m_star * M_SUN_IN_KG
        a_meters = (G_CONST * m_kg * p_sec**2 / (4.0 * np.pi**2))**(1.0 / 3.0)
        a_au = a_meters / AU_IN_METERS
        # Uncertainty: da/a = 1/3 * dM/M
        a_au_err = a_au * (1.0 / 3.0) * (m_star_err / m_star)

        # 3. Stellar Luminosity relative to Sun: L = (R_*)^2 * (T_* / 5777)^4
        l_star = (r_star**2) * ((teff_star / 5777.0)**4)

        # 4. Insolation Flux: S/S_earth = L_* / (a_au)^2
        insol_flux = l_star / (a_au**2)
        rel_err_insol = np.sqrt((2.0 * r_star_err / r_star)**2 + (4.0 * teff_star_err / teff_star)**2 + (2.0 * a_au_err / a_au)**2)
        insol_flux_err = insol_flux * rel_err_insol

        # 5. Equilibrium Temperature (assuming Bond albedo A_B = 0.3 and uniform redistribution)
        # Teq = Teff * sqrt(R* / 2a) * (1 - A_B)^(1/4)
        r_star_meters = r_star * R_SUN_IN_METERS
        teq_zero_albedo = teff_star * np.sqrt(r_star_meters / (2.0 * a_meters))
        teq_03_albedo = teq_zero_albedo * (1.0 - 0.3)**0.25
        teq_err = teq_03_albedo * np.sqrt((teff_star_err / teff_star)**2 + 0.25 * (r_star_err / r_star)**2 + 0.25 * (a_au_err / a_au)**2)

        # 6. Habitable Zone Classification (Kopparapu et al. 2013 limits)
        if insol_flux > 1.76:
            hz_status = "Too Hot (Interior to Recent Venus)"
        elif insol_flux >= 1.11:
            hz_status = "Optimistic Habitable Zone (Recent Venus - Runaway Greenhouse)"
        elif insol_flux >= 0.35:
            hz_status = "Conservative Habitable Zone (Runaway - Maximum Greenhouse)"
        elif insol_flux >= 0.32:
            hz_status = "Optimistic Habitable Zone (Maximum Greenhouse - Early Mars)"
        else:
            hz_status = "Too Cold (Beyond Early Mars)"

        # 7. Planetary regime classification
        if rp_earth < 1.25:
            regime = "Terrestrial (Rocky Earth-analog)"
        elif rp_earth < 2.0:
            regime = "Super-Earth"
        elif rp_earth < 4.0:
            regime = "Sub-Neptune"
        elif rp_earth < 10.0:
            regime = "Neptune-like / Ice Giant"
        elif rp_earth <= 25.0:
            regime = "Jovian / Gas Giant"
        else:
            regime = "Very Large Impostor (Likely Stellar Companion / EB)"

        return {
            "planet_radius_earth": float(rp_earth),
            "planet_radius_earth_err": float(rp_earth_err),
            "planet_radius_jup": float(rp_jup),
            "planet_radius_jup_err": float(rp_jup_err),
            "semi_major_axis_au": float(a_au),
            "semi_major_axis_au_err": float(a_au_err),
            "stellar_luminosity_solar": float(l_star),
            "insolation_flux_earth": float(insol_flux),
            "insolation_flux_earth_err": float(insol_flux_err),
            "equilibrium_temp_k": float(teq_03_albedo),
            "equilibrium_temp_k_err": float(teq_err),
            "equilibrium_temp_zero_albedo_k": float(teq_zero_albedo),
            "habitable_zone_status": hz_status,
            "physical_regime": regime
        }

def estimate_parameters(rp_rs, rp_rs_err, period_days, r_star=1.0, r_star_err=0.05,
                        m_star=1.0, m_star_err=0.08, teff_star=5777.0, teff_star_err=100.0):
    return ParameterEstimation.estimate(
        rp_rs, rp_rs_err, period_days, r_star, r_star_err, m_star, m_star_err, teff_star, teff_star_err
    )
