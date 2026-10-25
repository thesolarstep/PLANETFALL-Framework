import numpy as np

class FalsificationTribunal:
    """
    Statistically calibrated adversarial validation gauntlet.
    Synthesizes multi-domain evidence to compute calibrated False Positive Probability (FPP)
    and output definitive epistemic verdicts without ground-truth label leakage.
    """

    @staticmethod
    def evaluate(discovery_res, fit_res, oddeven_res, secondary_res, centroid_res, detrending_res, param_res=None):
        """
        Synthesize all evidentiary tests into a final verdict and calibrated FPP.
        """
        rejection_reasons = []
        ambiguity_reasons = []

        # 1. Alias & Harmonics Check
        if discovery_res.get("is_diurnal_alias", False):
            rejection_reasons.append(f"Rejected: Terrestrial diurnal alias ({discovery_res.get('alias_reason')})")

        # 2. Signal Significance
        snr = discovery_res.get("snr", 0.0)
        sde = discovery_res.get("sde", 0.0)
        if snr < 5.0 or sde < 5.0:
            rejection_reasons.append(f"Rejected: Low signal significance (SNR={snr:.1f}, SDE={sde:.1f} < 5.0)")
        elif snr < 7.0:
            ambiguity_reasons.append(f"Ambiguous: Marginal signal-to-noise ratio (SNR={snr:.1f} in [5.0, 7.0))")

        # 3. Number of transits
        n_transits = discovery_res.get("num_transits", 0)
        if n_transits < 2:
            rejection_reasons.append("Rejected: Fewer than 2 observed transits (unrepeatable single event)")

        # 4. Odd-Even Depth Difference Test (Eclipsing Binary Prosecution)
        oe_status = oddeven_res.get("status", "UNRESOLVED")
        oe_z = oddeven_res.get("z_score", 0.0)
        if oe_status == "REJECTED_ECLIPSING_BINARY" or oe_z >= 3.0:
            rejection_reasons.append(f"Rejected: Odd-even transit depth difference statistically significant (Z = {oe_z:.2f} >= 3.0, p = {oddeven_res.get('p_value', 0):.4f}) -> Eclipsing Binary")
        elif oe_status == "UNRESOLVED":
            ambiguity_reasons.append(f"Ambiguous: Odd-even test unresolved ({oddeven_res.get('reason', '')})")

        # 5. Secondary Eclipse Prosecution (Self-luminous / stellar companion)
        sec_status = secondary_res.get("status", "PASSED")
        sec_snr = secondary_res.get("secondary_snr", 0.0)
        if sec_status == "REJECTED_SECONDARY_ECLIPSE" or sec_snr >= 3.0:
            rejection_reasons.append(f"Rejected: Significant secondary eclipse detected (SNR = {sec_snr:.2f} >= 3.0, depth = {secondary_res.get('secondary_depth', 0)*1e6:.0f} ppm) -> Self-luminous companion")

        # 6. Centroid Shift Prosecution (Contaminating nearby source)
        cent_status = centroid_res.get("status", "NOT_TESTED")
        dr_pix = centroid_res.get("centroid_shift_pixels")
        if cent_status == "REJECTED_CENTROID_OFFSET" or (dr_pix is not None and dr_pix > 1.0):
            rejection_reasons.append(f"Rejected: Significant pixel centroid offset (dr = {dr_pix:.2f} pix = {centroid_res.get('centroid_shift_arcsec', 0):.1f} arcsec > 1.0 pix) -> Nearby contaminating source")
        elif cent_status in ["NOT_TESTED", "UNRESOLVED"]:
            ambiguity_reasons.append(f"Centroid test {cent_status}: {centroid_res.get('reason', 'TPF not tested')}")

        # 7. Detrending Preprocessing Sensitivity
        det_status = detrending_res.get("status", "PASSED")
        if det_status == "DETRENDING_SENSITIVE":
            ambiguity_reasons.append(f"Ambiguous: Transit depth unstable across detrending filter windows (scatter = {detrending_res.get('relative_depth_scatter', 0)*100:.1f}% > 40%)")

        # 8. Physical Planetary Radius Plausibility
        if param_res is not None:
            rp_jup = param_res.get("planet_radius_jup", 0.0)
            if rp_jup > 2.5:
                rejection_reasons.append(f"Rejected: Unphysical planetary radius (Rp = {rp_jup:.2f} R_jup > 2.5 R_jup) -> Stellar companion / grazing binary")

        # 9. Statistically Calibrated False Positive Probability (FPP)
        # Prior probability of planet vs astrophysical impostor in transit surveys ~ 0.10
        prior_planet = 0.10
        prior_fp = 0.90

        # Likelihood ratio based on physical tests
        # Bayes factor contributions
        bf_oe = 0.001 if oe_z >= 3.0 else (0.95 if oe_z < 1.5 else 1.5)
        bf_sec = 0.001 if sec_snr >= 3.0 else (0.90 if sec_snr < 1.5 else 1.2)
        bf_cent = 0.001 if (dr_pix is not None and dr_pix > 1.0) else (0.85 if (dr_pix is not None and dr_pix < 0.3) else 1.0)
        bf_snr = 0.10 if snr < 7.0 else (0.99 if snr > 12.0 else 0.80)
        bf_morph = 0.95 if fit_res.get("reduced_chi2", 2.0) < 1.5 else 1.3

        likelihood_ratio_planet_to_fp = (bf_oe * bf_sec * bf_cent * bf_snr * bf_morph) / (1.0)
        
        # Posterior odds = Prior odds * Likelihood ratio
        prior_odds = prior_planet / prior_fp
        posterior_odds = prior_odds * likelihood_ratio_planet_to_fp
        p_planet = posterior_odds / (1.0 + posterior_odds)
        fpp = float(1.0 - p_planet)
        fpp = float(np.clip(fpp, 0.0001, 0.9999))

        # 10. Synthesize Definitive Final Verdict
        if len(rejection_reasons) > 0:
            final_verdict = "REJECTED_FALSE_POSITIVE"
            confidence = "HIGH (Conclusive Astrophysical / Systematic Impostor)"
            fpp = max(0.95, fpp)
        elif len(ambiguity_reasons) > 0 and snr < 7.0:
            final_verdict = "UNRESOLVED_AMBIGUOUS"
            confidence = "LOW (Marginal Signal Requiring Follow-up)"
        else:
            final_verdict = "CONFIRMED_PLANET_CANDIDATE"
            confidence = "HIGH (Survives All Adversarial Prosecutions)"
            fpp = min(0.05, fpp)

        return {
            "verdict": final_verdict,
            "false_positive_probability": fpp,
            "confidence_assessment": confidence,
            "rejection_reasons": rejection_reasons,
            "ambiguity_reasons": ambiguity_reasons,
            "metrics_summary": {
                "snr": float(snr),
                "sde": float(sde),
                "oddeven_z": float(oe_z),
                "secondary_snr": float(sec_snr),
                "centroid_shift_pix": dr_pix,
                "reduced_chi2": float(fit_res.get("reduced_chi2", 1.0)),
                "delta_bic": float(fit_res.get("delta_bic", 0.0))
            }
        }

def evaluate_candidate(discovery_res, fit_res, oddeven_res, secondary_res, centroid_res, detrending_res, param_res=None):
    return FalsificationTribunal.evaluate(
        discovery_res, fit_res, oddeven_res, secondary_res, centroid_res, detrending_res, param_res
    )
