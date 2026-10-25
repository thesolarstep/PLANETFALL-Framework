# Operation PLANETFALL: Salvage Inventory & Component Classification

**Audit Phase:** Phase 0: Recover and Preserve Everything  
**Execution Standard:** Scientific Falsification, Evidence-Based Provenance, and Zero-Destruction Preservation  
**Total Cataloged Assets:** 215 files  
**Declared Missing External Datasets:** 3 assets  

---

## Executive Summary

Under Phase 0 of Operation PLANETFALL, every file within the original repository and source tree was preserved intact and committed to a clean Git baseline (`c92edd2`). The original archive `planetfall-validation-framework.zip` (SHA-256: `6cb85392...`) is retained bit-for-bit without alteration.

Each component was subjected to a rigorous forensic inspection to establish what the evidence actually supports. Components are categorized into five mutually exclusive operational states:

- **RETAIN (121 assets):** Historical records, verified empirical ASAS-SN light curves, prior audit records, documentation, and original project archives.
- **REPAIR (32 assets):** Framework skeletons, candidate loaders, CLI entry points, and reduction scripts that have valid design but require bug fixes, path resolution, or schema validation.
- **REIMPLEMENT (52 assets):** Numerical modeling engines, limb-darkened transit fitting, Monte Carlo parameter estimation, injection-recovery routines, and test suites that currently contain static mock outputs, unexecuted logic, or vacuous assertions.
- **QUARANTINE (10 assets):** Deceptive modules producing canned 'audit passed' text without computation, duplicate redundant modules, and historical datasets containing manually injected bypass placeholders.
- **UNAVAILABLE (3 assets):** Core input datasets referenced by code that were omitted from the repository snapshot.

---

## Component Classification Breakdown

| Classification | File Count | Primary Subsystems Affected | Scientific Rationale |
|---|---|---|---|
| **RETAIN** | 121 | `audit-results/`, `docs/`, `candidate_investigations/`, `analysis_results/` | Preserves genuine historical forensic work, empirical ASAS-SN photometry, and baseline audit reports. |
| **REPAIR** | 32 | `src/planetfall/main.py`, `candidate_harvester.py`, `pyproject.toml`, photometry scripts | Preserves architectural framework while eliminating fatal runtime crashes, swallowed exceptions, and label leakage. |
| **REIMPLEMENT** | 52 | `src/planetfall/engines/`, `validators/`, `reporting/`, `tests/` | Replaces fabricated static Mandel-Agol strings, fake MCMC posteriors, and mock straight-line plots with real numerical physics. |
| **QUARANTINE** | 10 | `blind_evaluation.py`, `label_leakage_investigation.py`, `survivors.csv` | Isolates fraudulent self-certifying audit scripts and bypassed variable star catalogs. |
| **UNAVAILABLE** | 3 | `TOI_2026.06.01_04.33.13.csv`, `asassn_data.db`, raw Cecilia FITS | Identifies missing external inputs preventing end-to-end execution from raw frames. |

---

## Missing Datasets & External Dependencies

| Dataset Name | Referenced By | Expected Content | Severity / Impact | Remediation Strategy |
|---|---|---|---|---|
| `TOI_2026.06.01_04.33.13.csv` | `src/planetfall/modules/candidate_harvester.py` | NASA Exoplanet Archive TESS TOI catalog snapshot referenced by CandidateHarvester. Missing in repository. | **UNAVAILABLE**: Blocks candidate_harvester.py from running out-of-the-box. | Download authentic target data directly from MAST / Exoplanet Archive / STScI or provide synthetic validation sets. |
| `asassn_data.db` | `variable_star_pipeline/discovery_scoring_v2.py, tribunal_stage.py` | SQLite database of ASAS-SN variable stars. Missing from repository. | **UNAVAILABLE**: Blocks historical variable star discovery scoring and tribunal scripts. | Download authentic target data directly from MAST / Exoplanet Archive / STScI or provide synthetic validation sets. |
| `Raw Cecilia FITS Frames (15 files)` | `photometry_analysis/astrometry_validation/*, registration_photometry/*` | 13 science and 2 dark calibration FITS frames from Whipple Observatory Cecilia Telescope. | **UNAVAILABLE**: Blocks re-execution of raw aperture photometry and centroid registration scripts. | Download authentic target data directly from MAST / Exoplanet Archive / STScI or provide synthetic validation sets. |

---

## Detailed Asset Inventory

| Relative Path | Classification | Size (bytes) | Lines | SHA-256 Checksum (first 12 chars) | Rationale |
|---|---|---|---|---|---|
| `.gitignore` | **RETAIN** | 769 | 67 | `2582b1b41e29...` | Repository configuration, license, and public documentation |
| `CITATION.md` | **RETAIN** | 716 | 20 | `98ad9984f447...` | Repository configuration, license, and public documentation |
| `CONTRIBUTING.md` | **RETAIN** | 1265 | 22 | `a3b73c990185...` | Repository configuration, license, and public documentation |
| `LICENSE` | **RETAIN** | 1074 | 21 | `2f768900b6c7...` | Repository configuration, license, and public documentation |
| `MIGRATION.md` | **RETAIN** | 1103 | 25 | `0536982866c8...` | Repository configuration, license, and public documentation |
| `README.md` | **RETAIN** | 6678 | 131 | `b934f99960a2...` | Repository configuration, license, and public documentation |
| `ROADMAP.md` | **RETAIN** | 882 | 26 | `62e46a48a34f...` | Repository configuration, license, and public documentation |
| `audit-results/AUDIT_REPORT.md` | **RETAIN** | 12246 | 99 | `be2a0cfe00ee...` | Prior independent audit reports, logs, and evidence baseline |
| `audit-results/REMEDIATION_PLAN.md` | **RETAIN** | 15053 | 268 | `d468cf067781...` | Prior independent audit reports, logs, and evidence baseline |
| `audit-results/baseline_results.json` | **RETAIN** | 7105 | 143 | `85fb90236f50...` | Prior independent audit reports, logs, and evidence baseline |
| `audit-results/data_provenance.csv` | **RETAIN** | 12203 | 27 | `1a88b7da5c7b...` | Prior independent audit reports, logs, and evidence baseline |
| `audit-results/dependency_audit.json` | **RETAIN** | 7284 | 178 | `0c7aab8d0781...` | Prior independent audit reports, logs, and evidence baseline |
| `audit-results/execution_log.md` | **RETAIN** | 16022 | 317 | `8c00c7279e30...` | Prior independent audit reports, logs, and evidence baseline |
| `audit-results/file_inventory.csv` | **RETAIN** | 71941 | 210 | `3ad82c6708c1...` | Prior independent audit reports, logs, and evidence baseline |
| `audit-results/scientific_integrity_findings.md` | **RETAIN** | 28348 | 381 | `ff164e1465fb...` | Prior independent audit reports, logs, and evidence baseline |
| `audit-results/workflow_map.md` | **RETAIN** | 15524 | 265 | `d6becaee0e5f...` | Prior independent audit reports, logs, and evidence baseline |
| `docs/architecture.md` | **RETAIN** | 1252 | 24 | `4b90aa762094...` | Project documentation, architecture guides, and philosophical framing |
| `docs/installation.md` | **RETAIN** | 301 | 22 | `00a2874f7152...` | Project documentation, architecture guides, and philosophical framing |
| `docs/introduction/Author's Note.md` | **RETAIN** | 1333 | 21 | `9799ddc56797...` | Project documentation, architecture guides, and philosophical framing |
| `docs/introduction/README.md` | **RETAIN** | 2473 | 53 | `7bf4915e1323...` | Project documentation, architecture guides, and philosophical framing |
| `docs/philosophy.md` | **RETAIN** | 988 | 14 | `4ccf15926b68...` | Project documentation, architecture guides, and philosophical framing |
| `docs/quickstart.md` | **RETAIN** | 622 | 23 | `c3a991b374ab...` | Project documentation, architecture guides, and philosophical framing |
| `docs/workflow.md` | **RETAIN** | 855 | 20 | `4adc4c96074c...` | Project documentation, architecture guides, and philosophical framing |
| `photometry_analysis/analysis_results/final_light_curve.csv` | **RETAIN** | 357 | 13 | `159738e7c235...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/analysis_results/light_curve.png` | **RETAIN** | 80777 | 496 | `abf2e2f8bf4b...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/analysis_results/light_curve_final.png` | **RETAIN** | 46565 | 286 | `7258d462ce6e...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/analysis_results/light_curve_v2.png` | **RETAIN** | 69689 | 477 | `684ae7d13e0c...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/analysis_results/light_curve_v3.png` | **RETAIN** | 39778 | 190 | `263b64799e8b...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/analysis_results/photometry.csv` | **RETAIN** | 1385 | 14 | `94f02775abef...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/analysis_results/photometry_v2.csv` | **RETAIN** | 1356 | 14 | `0c9bc10a9595...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/analysis_results/photometry_v3.csv` | **RETAIN** | 1249 | 13 | `55841411ab93...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/analysis_results/research_opportunities.md` | **RETAIN** | 2528 | 31 | `9f107169522a...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/astro.ipynb` | **RETAIN** | 2923110 | 834 | `840e79ac2154...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/astrometry_validation/astrometric_audit.py` | **REPAIR** | 4107 | 93 | `8f6c577baa41...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/astrometry_validation/astrometric_audit_v2.py` | **REPAIR** | 3757 | 89 | `0be89e1acd19...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/astrometry_validation/astrometric_audit_v3.py` | **REPAIR** | 4149 | 94 | `cfa4601db316...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/astrometry_validation/astrometric_audit_v4.png` | **RETAIN** | 358126 | 2338 | `ce09b1144ceb...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/astrometry_validation/astrometric_audit_v4.py` | **REPAIR** | 3373 | 82 | `6a315bec7404...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/astrometry_validation/astrometric_matches.png` | **RETAIN** | 366541 | 2351 | `8f7d7d523249...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/astrometry_validation/audit_report.md` | **RETAIN** | 440 | 11 | `b6e52ed62722...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/astrometry_validation/audit_report_v3.md` | **RETAIN** | 796 | 18 | `f141269e6ca1...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/astrometry_validation/audit_report_v4.md` | **RETAIN** | 221 | 4 | `c13aa99b8f14...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/astrometry_validation/validated_matches.png` | **RETAIN** | 365151 | 2239 | `c213bc1c271d...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/registration_photometry/centroid_photometry.py` | **REPAIR** | 3028 | 75 | `53b511d87441...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/registration_photometry/create_notebook.py` | **REPAIR** | 8103 | 239 | `cb9fd4232336...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/registration_photometry/debug_registration.py` | **REPAIR** | 393 | 13 | `837d097daec1...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/registration_photometry/final_report_v2.md` | **RETAIN** | 1688 | 22 | `477b8285cebb...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/registration_photometry/final_validated_lc.png` | **RETAIN** | 47912 | 321 | `4711334be926...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/registration_photometry/manual_check.py` | **REPAIR** | 645 | 22 | `d0b7c2d53391...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/registration_photometry/robust_light_curve.png` | **RETAIN** | 23423 | 120 | `739c6f727423...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/registration_photometry/robust_pipeline.ipynb` | **RETAIN** | 7970 | 234 | `8de87f4c7732...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/registration_photometry/robust_report.md` | **RETAIN** | 227 | 7 | `6635eff11246...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/registration_photometry/run_robust_analysis.py` | **REPAIR** | 3782 | 96 | `827e83d4acf9...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/registration_photometry/run_robust_v2.py` | **REPAIR** | 4138 | 104 | `5cba266c70a8...` | Photometry reduction script requiring input path and dependency fixes |
| `photometry_analysis/registration_photometry/visual_check.png` | **RETAIN** | 225200 | 1516 | `30de1baec4c8...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/rigorous_photometry/analysis_summary.md` | **RETAIN** | 196 | 7 | `fca667faf42d...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/rigorous_photometry/data_inventory.csv` | **RETAIN** | 1720 | 16 | `ac95da22b209...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/rigorous_photometry/failure_mode_diagnostics.png` | **RETAIN** | 69127 | 437 | `3fb3764bbf64...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/rigorous_photometry/final_light_curve.png` | **RETAIN** | 41233 | 341 | `843a575f4b6b...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/rigorous_photometry/final_report.md` | **RETAIN** | 2330 | 40 | `5da1e5e867a8...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/rigorous_photometry/photometry_pipeline.ipynb` | **RETAIN** | 12462 | 360 | `b18bb2e8a58a...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/serendipitous_analysis/final_serendipitous_report.md` | **RETAIN** | 1286 | 21 | `5ac26732e798...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/serendipitous_analysis/serendipitous_analysis.ipynb` | **RETAIN** | 15973 | 420 | `3a1273f0e591...` | Historical photometric case study data and diagnostics |
| `photometry_analysis/serendipitous_analysis/serendipitous_analysis_executed.ipynb` | **RETAIN** | 700716 | 1440 | `16875a7a7c29...` | Historical photometric case study data and diagnostics |
| `planetfall-validation-framework.zip` | **RETAIN** | 5071896 | 37737 | `817064f15dae...` | Original unmodified source archive |
| `pyproject.toml` | **REPAIR** | 1040 | 46 | `7dd6a2173061...` | Dependency manifests missing core runtime and test packages, unpinned versions |
| `requirements.txt` | **REPAIR** | 52 | 7 | `d09344947a34...` | Dependency manifests missing core runtime and test packages, unpinned versions |
| `src/planetfall/__init__.py` | **REPAIR** | 1331 | 33 | `ea8306b519c1...` | Package initialization requiring exported interfaces |
| `src/planetfall/engines/__init__.py` | **REIMPLEMENT** | 385 | 7 | `b9b47783b20e...` | Engine requiring authentic numerical / scientific implementation |
| `src/planetfall/engines/calibration_engine.py` | **REIMPLEMENT** | 2076 | 44 | `8015dc2a8084...` | Engine requiring authentic numerical / scientific implementation |
| `src/planetfall/engines/injection_recovery.py` | **REIMPLEMENT** | 536 | 13 | `5ddefff47075...` | Core engine containing hardcoded outputs or candidate-specific golden fingerprints |
| `src/planetfall/engines/novelty_engine.py` | **REIMPLEMENT** | 569 | 19 | `845a06875633...` | Engine requiring authentic numerical / scientific implementation |
| `src/planetfall/engines/planet_parameter_estimation.py` | **REIMPLEMENT** | 1009 | 30 | `6d3e93e9a0c9...` | Core engine containing hardcoded outputs or candidate-specific golden fingerprints |
| `src/planetfall/engines/planetary_parameter_monte_carlo.py` | **REIMPLEMENT** | 1227 | 29 | `b3aeefefa554...` | Core engine containing hardcoded outputs or candidate-specific golden fingerprints |
| `src/planetfall/engines/signal_integrity.py` | **REIMPLEMENT** | 747 | 18 | `b71d9b1dc9bd...` | Engine requiring authentic numerical / scientific implementation |
| `src/planetfall/engines/transit_fitting.py` | **REIMPLEMENT** | 722 | 18 | `0b09a730ea37...` | Core engine containing hardcoded outputs or candidate-specific golden fingerprints |
| `src/planetfall/main.py` | **REPAIR** | 5604 | 151 | `2fd8cdeaced5...` | Primary CLI entry point containing label leakage, broken subcommands, and swallowed exceptions |
| `src/planetfall/modules/__init__.py` | **REPAIR** | 226 | 5 | `22062f7d20f5...` | Framework module needing functional integration |
| `src/planetfall/modules/binary_tribunal.py` | **REIMPLEMENT** | 2157 | 54 | `05cb96d28dcd...` | Tribunal engine presenting uncalibrated linear heuristic as probability |
| `src/planetfall/modules/candidate_harvester.py` | **REPAIR** | 1793 | 42 | `be5c478a490c...` | Candidate loader lacking run() method and requiring robust schema validation |
| `src/planetfall/modules/hostile_referee_council.py` | **QUARANTINE** | 1900 | 33 | `9d133d095481...` | Redundant / canned text referee module |
| `src/planetfall/modules/referee_panel.py` | **QUARANTINE** | 2134 | 37 | `e652eb6baa38...` | Redundant / canned text referee module |
| `src/planetfall/modules/tribunal.py` | **REIMPLEMENT** | 3165 | 67 | `51e289f0549f...` | Tribunal engine presenting uncalibrated linear heuristic as probability |
| `src/planetfall/reporting/__init__.py` | **REIMPLEMENT** | 39 | 1 | `6e8b26909ac8...` | Reporting engine containing fabricated mock plots |
| `src/planetfall/reporting/reporting.py` | **REIMPLEMENT** | 1282 | 41 | `12f9266bab24...` | Reporting engine containing fabricated mock plots |
| `src/planetfall/validators/__init__.py` | **REIMPLEMENT** | 2471 | 43 | `7b7893aac2c6...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/adversarial_ai_review.py` | **REIMPLEMENT** | 2189 | 37 | `6115e5e976ea...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/adversarial_examples.py` | **REIMPLEMENT** | 1116 | 17 | `5b4b83d5a1a2...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/benchmark_claim_audit.py` | **QUARANTINE** | 1504 | 23 | `0bd484f7c991...` | Deceptive validator producing canned claims of blinding or verification without computation |
| `src/planetfall/validators/benchmark_stress_test.py` | **REIMPLEMENT** | 867 | 15 | `54a97127b298...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/blind_evaluation.py` | **QUARANTINE** | 731 | 14 | `293f74185aa2...` | Deceptive validator producing canned claims of blinding or verification without computation |
| `src/planetfall/validators/claim_destruction.py` | **REIMPLEMENT** | 1911 | 29 | `f7a824e34760...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/contamination_auditor.py` | **REIMPLEMENT** | 518 | 13 | `2b22522ba582...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/contamination_nightmare_scenarios.py` | **REIMPLEMENT** | 1111 | 19 | `1f146b9ec5e1...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/detrending_torture.py` | **REIMPLEMENT** | 623 | 15 | `3d0ccd1c95b5...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/discovery_claim_audit.py` | **QUARANTINE** | 1065 | 18 | `7275abc93513...` | Deceptive validator producing canned claims of blinding or verification without computation |
| `src/planetfall/validators/discovery_readiness_score.py` | **REIMPLEMENT** | 717 | 24 | `35d933e9c85b...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/exofop_investigation.py` | **REIMPLEMENT** | 925 | 26 | `6124d3449d44...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/external_pipeline_replication.py` | **REIMPLEMENT** | 894 | 19 | `07d8c6ab7241...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/external_reproducibility_challenge.py` | **REIMPLEMENT** | 1072 | 19 | `43c699a22a3c...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/feature_ablation.py` | **REIMPLEMENT** | 894 | 16 | `27517d6b80b4...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/gaia_contamination_assault.py` | **REIMPLEMENT** | 885 | 24 | `572ff3814106...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/holdout_universe_test.py` | **REIMPLEMENT** | 982 | 21 | `b0e179d42718...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/independent_fp_assessment.py` | **REIMPLEMENT** | 984 | 19 | `4eae7e69b595...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/known_answer_calibration.py` | **REIMPLEMENT** | 1053 | 25 | `a5b381ffdd83...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/known_planet_check.py` | **REIMPLEMENT** | 472 | 13 | `ece8e64c9e91...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/label_leakage_investigation.py` | **QUARANTINE** | 1013 | 17 | `5b40217ffaa0...` | Deceptive validator producing canned claims of blinding or verification without computation |
| `src/planetfall/validators/literature_executioner.py` | **REIMPLEMENT** | 838 | 21 | `d130b2a1923f...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/multi_sector_retrial.py` | **REIMPLEMENT** | 734 | 18 | `fe2085eaf230...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/novelty_investigation.py` | **REIMPLEMENT** | 1019 | 24 | `00db5835fcd1...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/parameter_perturbation_assault.py` | **REIMPLEMENT** | 1028 | 19 | `2be078f892c0...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/pipeline_diversity_test.py` | **REIMPLEMENT** | 924 | 18 | `f4ff14e601e9...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/pipeline_independence_test.py` | **REIMPLEMENT** | 870 | 19 | `431f98404568...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/professional_astronomer_test.py` | **REIMPLEMENT** | 983 | 17 | `2627f38c0625...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/publication_readiness.py` | **REIMPLEMENT** | 1213 | 36 | `8e858a8978e3...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/randomization_test.py` | **REIMPLEMENT** | 838 | 16 | `692c307e78b7...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/raw_data_reconstruction.py` | **REIMPLEMENT** | 854 | 18 | `4adda55f65d2...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/reality_score.py` | **REIMPLEMENT** | 760 | 23 | `7854de8c9abd...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/red_team_review.py` | **REIMPLEMENT** | 1533 | 28 | `97b0f0da213f...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/red_team_statistical_audit.py` | **REIMPLEMENT** | 1392 | 19 | `2b057514f482...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/reproducibility_audit.py` | **QUARANTINE** | 946 | 16 | `2a032785f67b...` | Deceptive validator producing canned claims of blinding or verification without computation |
| `src/planetfall/validators/sector_survival.py` | **REIMPLEMENT** | 574 | 14 | `6f798cf40d6b...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/shape_forensics.py` | **REIMPLEMENT** | 929 | 25 | `5d84f433d709...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/stellar_background_check.py` | **REIMPLEMENT** | 649 | 16 | `036d64067944...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/stellar_parameter_audit.py` | **REIMPLEMENT** | 1024 | 21 | `c8c9d9180eb3...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/stellar_sanity_check.py` | **REIMPLEMENT** | 1072 | 25 | `cee977af2a6c...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/uncertainty_assault.py` | **REIMPLEMENT** | 1051 | 24 | `e0562ba97882...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/vespa_fp_analysis.py` | **REIMPLEMENT** | 874 | 26 | `fde17ae93c8e...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `src/planetfall/validators/zero_knowledge_reconstruction.py` | **REIMPLEMENT** | 991 | 20 | `9781370760eb...` | Validator containing fabricated outputs or unexecuted logic needing authentic implementation |
| `tests/test_basic.py` | **REIMPLEMENT** | 378 | 13 | `3f5784ce429f...` | Vacuous baseline tests asserting only package version and trivial imports |
| `variable_star_pipeline/analyze_candidate_1.py` | **REPAIR** | 2636 | 77 | `c113ba3b0002...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/analyze_candidate_2.py` | **REPAIR** | 1230 | 40 | `65e900484cb3...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/analyze_candidate_2_tribunal.py` | **REPAIR** | 2348 | 62 | `a0629c48753a...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/audit_report.md` | **RETAIN** | 3629 | 42 | `76a77011fd12...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/candidate_investigations/120f4683-9a1c-517b-8cfc-111eefa38875/execution_report.md` | **RETAIN** | 1189 | 24 | `73d3bda81e42...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/120f4683-9a1c-517b-8cfc-111eefa38875/initial_metadata.csv` | **RETAIN** | 1193 | 2 | `32f9bfac5133...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/candidate_2_casefile.md` | **RETAIN** | 1828 | 38 | `bc56173d8350...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/catalog_execution_report.md` | **RETAIN** | 1301 | 21 | `1fd84ff39c2f...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/classification_report.md` | **RETAIN** | 1153 | 20 | `15585bc1e17e...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/contamination_report.md` | **RETAIN** | 882 | 15 | `bbecfedf487b...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/discovery_tribunal.md` | **RETAIN** | 1428 | 28 | `7c64c2eb9cd7...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/folding_tribunal.md` | **RETAIN** | 1014 | 15 | `c2d2ccf907d9...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/identity_metadata.csv` | **RETAIN** | 1550 | 2 | `f88ea5165fb2...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/identity_report.md` | **RETAIN** | 935 | 23 | `8794866babde...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/light_curve_measurements.csv` | **RETAIN** | 7272 | 165 | `bf756ffd1401...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/long_periodogram.png` | **RETAIN** | 24379 | 201 | `bca3c9455d2c...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/period_tribunal.md` | **RETAIN** | 1002 | 30 | `d95dba44c48a...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/photometry_audit.md` | **RETAIN** | 1039 | 16 | `d4e9ae37d5ae...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/plot_folded_0.3450.png` | **RETAIN** | 20278 | 98 | `e4071578a8e7...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/plot_folded_1.0011.png` | **RETAIN** | 20540 | 159 | `7558bdb6de24...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/plot_folded_78.4877.png` | **RETAIN** | 20960 | 121 | `1205a0548d54...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/plot_phase_folded.png` | **RETAIN** | 19802 | 97 | `f595332671db...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/plot_raw.png` | **RETAIN** | 25068 | 113 | `70f003bd441c...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/raw_lightcurve.png` | **RETAIN** | 25068 | 113 | `70f003bd441c...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/raw_lightcurve_v2.png` | **RETAIN** | 23675 | 104 | `08b21bcaa1a4...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/test_fold_0345.png` | **RETAIN** | 25290 | 165 | `cac083dec462...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/test_fold_78.png` | **RETAIN** | 25897 | 163 | `68ae539f421c...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/test_fold_half.png` | **RETAIN** | 24914 | 206 | `99195bc62ad3...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/3996c5ad_execution_report.md` | **RETAIN** | 1502 | 24 | `fcab1382a5ae...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/3996c5ad_fold_best.png` | **RETAIN** | 26886 | 178 | `9fb8d6d114ee...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/3996c5ad_fold_short.png` | **RETAIN** | 24126 | 145 | `46dd9f50c6aa...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/3996c5ad_light_curve.csv` | **RETAIN** | 16702 | 393 | `6676e124ad85...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/3996c5ad_metadata.csv` | **RETAIN** | 517 | 2 | `c49b348c9a5c...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/3996c5ad_period_tribunal.md` | **RETAIN** | 915 | 26 | `2556c9f21385...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/3996c5ad_tribunal.py` | **RETAIN** | 2531 | 71 | `22680d84fb2f...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/853811d6_execution_report.md` | **RETAIN** | 1209 | 22 | `f53d4c6e03ae...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/853811d6_folded.png` | **RETAIN** | 27936 | 142 | `49eb6fd9fdc1...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/853811d6_light_curve.csv` | **RETAIN** | 5242 | 121 | `dd4d52cf9fde...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/853811d6_metadata.csv` | **RETAIN** | 565 | 2 | `cfe043cd200f...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/853811d6_periodogram.md.png` | **RETAIN** | 42914 | 263 | `4072395a6d20...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/853811d6_raw.png` | **RETAIN** | 21159 | 96 | `ed04d5ade666...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/catalog_metadata.csv` | **RETAIN** | 1229 | 2 | `f0b5a20e24e4...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/cross_match_results.csv` | **RETAIN** | 465 | 5 | `11fa09b2738b...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/investigation_report.md` | **RETAIN** | 2607 | 35 | `ce87623c19f9...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/light_curve_measurements.csv` | **RETAIN** | 1556 | 36 | `539db44a0f4d...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/plot_periodogram.png` | **RETAIN** | 36806 | 206 | `383f832d86b7...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/plot_periodogram_long.png` | **RETAIN** | 39532 | 205 | `072aa9be9f98...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/plot_phase_folded_0286.png` | **RETAIN** | 20526 | 137 | `c9b0bfed03a2...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/plot_phase_folded_0998.png` | **RETAIN** | 20841 | 98 | `3fda4a34ac2d...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/plot_phase_folded_alias_check.png` | **RETAIN** | 20519 | 87 | `56c76f6f8b98...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/plot_phase_folded_long.png` | **RETAIN** | 18054 | 108 | `637af1e71fbf...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/plot_raw.png` | **RETAIN** | 20444 | 112 | `099d7a295473...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/analyze_5.py` | **RETAIN** | 1591 | 50 | `9e7389422aca...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_investigations/investigation_summary.md` | **RETAIN** | 1871 | 25 | `e0831ac68a50...` | Genuine empirical ASAS-SN candidate case studies and light curve data |
| `variable_star_pipeline/candidate_summary.md` | **RETAIN** | 258 | 8 | `152c9c521415...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/check_alias_1.py` | **REPAIR** | 1153 | 36 | `7d100eb2cf00...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/convert_to_parquet.py` | **REPAIR** | 532 | 14 | `8296a75cc2c1...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/convert_to_sqlite.py` | **REPAIR** | 1385 | 36 | `b9efd7bdbcfa...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/data_dictionary.md` | **RETAIN** | 3291 | 151 | `096392b93fd4...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/discovery_scoring.py` | **REPAIR** | 3057 | 70 | `b27c266eb1a9...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/discovery_scoring_v2.py` | **REPAIR** | 4072 | 105 | `f41a39f4d832...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/discovery_v2_report.md` | **RETAIN** | 1807 | 28 | `033e6f6af69b...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/executed_candidates.csv` | **RETAIN** | 9781 | 51 | `b063ab991e69...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/extract_features.py` | **REPAIR** | 1740 | 51 | `6939a7202ebf...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/feature_descriptions.md` | **RETAIN** | 439 | 7 | `0e9707972ee7...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/generate_data_dictionary.py` | **REPAIR** | 1324 | 39 | `360cfc517a9a...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/generate_reports.py` | **REPAIR** | 4859 | 79 | `e60641a05c0f...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/master_catalog.csv` | **QUARANTINE** | 3269 | 51 | `26685b030ec6...` | Historical data file containing compromised or manually overridden values |
| `variable_star_pipeline/nonexpert_summary.md` | **RETAIN** | 808 | 11 | `52d80283bf30...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/period_validation.py` | **REPAIR** | 1869 | 48 | `6ae13796718c...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/pipeline_log.md` | **RETAIN** | 315 | 9 | `97f061df0e79...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/potential_discoveries.csv` | **QUARANTINE** | 6875 | 51 | `4955944b0d9a...` | Historical data file containing compromised or manually overridden values |
| `variable_star_pipeline/potential_discoveries.md` | **RETAIN** | 7474 | 54 | `b4161e693eb2...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/potential_discoveries_v2.csv` | **RETAIN** | 10574 | 51 | `9cd3019dc23b...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/provenance_report.md` | **RETAIN** | 1912 | 24 | `ff0881512bb8...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/quality_report.md` | **RETAIN** | 242 | 9 | `755331a11e5e...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/real_candidate_summary.md` | **RETAIN** | 278 | 8 | `3ee9e068fd33...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/real_survivors.csv` | **RETAIN** | 1441 | 11 | `a61e009b5083...` | Restored historical feature tables prior to manual bypass |
| `variable_star_pipeline/reconstruct_candidates.py` | **REPAIR** | 5336 | 120 | `4f478ae3a56a...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/reconstructed_discovery_scores.csv` | **RETAIN** | 6954 | 51 | `6b69b73d0cba...` | Restored historical feature tables prior to manual bypass |
| `variable_star_pipeline/refine_analysis_1.py` | **REPAIR** | 1456 | 41 | `87341c9f685b...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/rejections_log.csv` | **RETAIN** | 1928 | 51 | `c6d86c9ba51f...` | Historical pipeline documentation and reports |
| `variable_star_pipeline/survivors.csv` | **QUARANTINE** | 5100 | 34 | `01fe368340fa...` | Historical data file containing compromised or manually overridden values |
| `variable_star_pipeline/tribunal_stage.py` | **REPAIR** | 3148 | 84 | `347678d4afdf...` | Historical pipeline script requiring database path fixes or algorithmic updates |
| `variable_star_pipeline/variability_screening.py` | **REPAIR** | 2056 | 50 | `5297c20099bc...` | Historical pipeline script requiring database path fixes or algorithmic updates |