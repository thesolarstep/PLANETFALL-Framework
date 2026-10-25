import os
import json
import numpy as np

def save_casefile(target_id, discovery_res, fit_res, oddeven_res, secondary_res,
                  centroid_res, detrending_res, param_res, tribunal_res,
                  diagnostic_plot_path, out_dir):
    """
    Saves candidate casefile in machine-readable JSON and formatted Markdown.
    """
    os.makedirs(out_dir, exist_ok=True)
    
    # Clean arrays from discovery_res and fit_res for JSON serialization
    disc_clean = {k: (v if not isinstance(v, (np.ndarray, list)) else len(v) if k.endswith("_grid") else v)
                  for k, v in discovery_res.items() if not k.endswith("_grid")}
    
    fit_clean = {k: v for k, v in fit_res.items() if k not in ["model_flux", "residuals"]}

    casefile_dict = {
        "target_id": str(target_id),
        "verdict": tribunal_res["verdict"],
        "false_positive_probability": tribunal_res["false_positive_probability"],
        "confidence": tribunal_res["confidence_assessment"],
        "rejection_reasons": tribunal_res["rejection_reasons"],
        "ambiguity_reasons": tribunal_res["ambiguity_reasons"],
        "discovery_metrics": disc_clean,
        "transit_model_fit": fit_clean,
        "odd_even_test": oddeven_res,
        "secondary_eclipse_test": secondary_res,
        "centroid_test": centroid_res,
        "detrending_sensitivity": detrending_res,
        "physical_parameters": param_res,
        "diagnostic_plot": diagnostic_plot_path
    }

    # Write JSON
    json_path = os.path.join(out_dir, f"{target_id}_casefile.json")
    with open(json_path, "w") as f:
        json.dump(casefile_dict, f, indent=2)

    # Write Markdown
    md_path = os.path.join(out_dir, f"{target_id}_casefile.md")
    md_lines = [
        f"# PLANETFALL Candidate Casefile: {target_id}",
        "",
        f"**Final Epistemic Verdict:** `{tribunal_res['verdict']}`  ",
        f"**False Positive Probability (FPP):** `{tribunal_res['false_positive_probability']:.4f}`  ",
        f"**Confidence Assessment:** {tribunal_res['confidence_assessment']}  ",
        "",
        "---",
        "",
        "## 1. Transit Detection & Morphology",
        f"- **Orbital Period:** `{discovery_res['period']:.6f}` days",
        f"- **Transit Center (T0):** `{discovery_res['t0']:.5f}` BJD/BTJD",
        f"- **Transit Duration:** `{discovery_res['duration_hours']:.2f}` hours ({discovery_res['duration_days']:.4f} days)",
        f"- **Transit Depth:** `{fit_res['depth']*1e6:.1f}` ppm ({fit_res['depth']*100:.3f}%)",
        f"- **Radius Ratio (Rp/Rs):** `{fit_res['rp_rs']:.4f} ± {fit_res['rp_rs_err']:.4f}`",
        f"- **Scaled Semi-major Axis (a/Rs):** `{fit_res['a_rs']:.2f} ± {fit_res['a_rs_err']:.2f}`",
        f"- **Orbital Inclination:** `{fit_res['inclination']:.2f}° ± {fit_res['inclination_err']:.2f}°`",
        f"- **Impact Parameter (b):** `{fit_res['impact_parameter']:.2f}`",
        f"- **Transit SNR:** `{discovery_res['snr']:.1f}`",
        f"- **Signal Detection Efficiency (SDE):** `{discovery_res['sde']:.1f}`",
        f"- **Reduced Chi-Square:** `{fit_res['reduced_chi2']:.2f}`",
        f"- **Delta BIC (Transit vs Flat):** `{fit_res['delta_bic']:.1f}`",
        "",
        "---",
        "",
        "## 2. Adversarial False-Positive Gauntlet",
        "",
        "| Prosecution Module | Result / Test Statistic | Verdict / Status | Scientific Interpretation |",
        "|---|---|---|---|",
        f"| **Odd-Even Depth Difference** | Z = {oddeven_res['z_score']:.2f} (p = {oddeven_res['p_value']:.4f}) | `{oddeven_res['status']}` | {'Consistent depths: no evidence of binary period doubling.' if oddeven_res['z_score'] < 3.0 else 'Significant depth mismatch: likely eclipsing binary.'} |",
        f"| **Secondary Eclipse Search** | SNR = {secondary_res['secondary_snr']:.2f}, Depth = {secondary_res['secondary_depth']*1e6:.0f} ppm | `{secondary_res['status']}` | {'No secondary eclipse detected; upper limit placed.' if secondary_res['status'] == 'PASSED' else 'Secondary eclipse detected: likely stellar companion.'} |",
        f"| **Pixel Centroid Shift (TPF)** | Offset = {centroid_res.get('centroid_shift_pixels', 'N/A')} pix ({centroid_res.get('centroid_shift_arcsec', 'N/A')} arcsec) | `{centroid_res['status']}` | {'Photocenter stays on target.' if centroid_res['status'] == 'PASSED' else ('Offset detected: background contaminant.' if centroid_res['status'] == 'REJECTED_CENTROID_OFFSET' else 'TPF not available / not tested.')} |",
        f"| **Detrending Preprocessing Sensitivity** | Scatter = {detrending_res['relative_depth_scatter']*100:.1f}% across filter windows | `{detrending_res['status']}` | {'Transit signal survives across filter bandwidths.' if detrending_res['status'] == 'PASSED' else 'Signal sensitive to filter window choice.'} |",
        "",
        "---",
        "",
        "## 3. Physical Exoplanetary Characteristics",
    ]

    if param_res:
        md_lines.extend([
            f"- **Planet Radius:** `{param_res['planet_radius_earth']:.2f} ± {param_res['planet_radius_earth_err']:.2f}` R_earth (`{param_res['planet_radius_jup']:.3f}` R_jup)",
            f"- **Physical Regime:** {param_res['physical_regime']}",
            f"- **Semi-major Axis:** `{param_res['semi_major_axis_au']:.4f} ± {param_res['semi_major_axis_au_err']:.4f}` AU",
            f"- **Insolation Flux:** `{param_res['insolation_flux_earth']:.2f} ± {param_res['insolation_flux_earth_err']:.2f}` S_earth",
            f"- **Equilibrium Temperature (A_B=0.3):** `{param_res['equilibrium_temp_k']:.1f} ± {param_res['equilibrium_temp_k_err']:.1f}` K",
            f"- **Habitable Zone Classification:** `{param_res['habitable_zone_status']}`",
            ""
        ])

    if tribunal_res["rejection_reasons"]:
        md_lines.extend([
            "### Rejection Summary",
            ""
        ])
        for r in tribunal_res["rejection_reasons"]:
            md_lines.append(f"- **[REJECTION]** {r}")
        md_lines.append("")

    if tribunal_res["ambiguity_reasons"]:
        md_lines.extend([
            "### Unresolved / Ambiguous Issues",
            ""
        ])
        for a in tribunal_res["ambiguity_reasons"]:
            md_lines.append(f"- **[NOTE]** {a}")
        md_lines.append("")

    md_lines.extend([
        "---",
        "",
        "## 4. Diagnostic Figure",
        f"![Validation Diagnostics]({diagnostic_plot_path})",
        "",
        "---",
        "*Report generated autonomously by PLANETFALL Discovery and Validation Engine.*"
    ])

    with open(md_path, "w") as f:
        f.write("\n".join(md_lines))

    return json_path, md_path
