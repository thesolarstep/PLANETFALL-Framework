# Phase 0 Reproducibility & Baseline Preservation Report

**Project:** OPERATION PLANETFALL  
**Date:** 2026-10-25  
**Baseline Git Commit:** `c92edd2`  
**Original Archive Checksum (SHA-256):** `planetfall-validation-framework.zip`  

---

## 1. Preservation Protocol

To ensure total forensic integrity, all repository assets have been committed to a local Git repository before making any alterations. The original zip archive `planetfall-validation-framework.zip` is preserved in the project root.

### Baseline Checksums of Critical Artifacts

| File | Size (Bytes) | SHA-256 Checksum |
|---|---|---|
| `planetfall-validation-framework.zip` | 5071896 | `817064f15daea09d2cefd14b0fa0f2ef7b1d186ec01a230c6eb4d94afb9bf8c0` |
| `src/planetfall/main.py` | 5604 | `2fd8cdeaced5ecf4d9927599687c41b446c961e1c1d9bfdce7934406685031c6` |
| `src/planetfall/modules/candidate_harvester.py` | 1793 | `be5c478a490c1eb38bf7d5c458c18f5c68af3b55ec368f5b305a334cfc3ee0a8` |
| `src/planetfall/engines/transit_fitting.py` | 722 | `0b09a730ea374abe823cc30337cea766de982cc9dc1b183ce1d6cd1f0a66bf69` |
| `src/planetfall/engines/planetary_parameter_monte_carlo.py` | 1227 | `b3aeefefa554e2a81154bb9eedf51f018e261b43f6be943be4253faa42259972` |
| `src/planetfall/engines/injection_recovery.py` | 536 | `5ddefff47075b701d72e24224247d93f64b926f3a6ed7f7bfcfffc4ebcc8b583` |
| `src/planetfall/engines/planet_parameter_estimation.py` | 1009 | `6d3e93e9a0c9a4790b7ad35f96dba67cbc42671729f898b07fe1a09e17652d32` |
| `audit-results/AUDIT_REPORT.md` | 12246 | `be2a0cfe00ee6b35a665c5dc068ba0bb3ab4ed950b769646df2a1bdfad801f38` |
| `audit-results/scientific_integrity_findings.md` | 28348 | `ff164e1465fbee98cc63ce06e2d54174ee810fdf2767ff65774ec2ed7d5a4cf9` |
| `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/investigation_report.md` | 2607 | `ce87623c19f91a640a1eb6d36d7c2ffecca558b5a0472e217361992ae3748d0d` |

---

## 2. Separation of Observations, Inferences, and Fabrications

A foundational requirement of Phase 0 is cleanly separating genuine astronomical data from simulated outputs, cached results, and fabricated mock values.

### Genuine Observational Assets
- **ASAS-SN Sky Patrol Time-Series Photometry:**
  - `variable_star_pipeline/candidate_investigations/9c44d67a-14fb-5f1a-ac17-65a03a20bb4e/light_curve_measurements.csv` (35 epochs)
  - `variable_star_pipeline/candidate_investigations/2514cd3c-f031-557d-b251-629a5efa2362/light_curve_measurements.csv` (164 epochs)
  - `variable_star_pipeline/candidate_investigations/3996c5ad_light_curve.csv` (392 epochs)
  - `variable_star_pipeline/candidate_investigations/853811d6_light_curve.csv` (120 epochs)
- **Extracted Differential Photometry Tables (Cecilia Telescope):**
  - `photometry_analysis/analysis_results/photometry.csv`, `photometry_v2.csv`, `photometry_v3.csv`, `final_light_curve.csv` (12-13 photometric epochs from 2026-05-29/30 TrES-5 transit observation run).

### Fabricated and Mock Outputs (Quarantined / Targeted for Reimplementation)
- **`src/planetfall/engines/transit_fitting.py`:** Hardcoded markdown claiming $R_p/R_* = 0.021 \pm 0.002$ and inclination $88.5^\circ$ for any input candidate.
- **`src/planetfall/engines/planetary_parameter_monte_carlo.py`:** Hardcoded static MCMC posterior table claiming 10,000 iterations without running any sampler.
- **`src/planetfall/engines/injection_recovery.py`:** Hardcoded static recovery table claiming 95% recovery across all SNR bins.
- **`src/planetfall/reporting/reporting.py`:** Generates straight lines with synthetic Gaussian noise rather than plotting actual candidate light curves.
- **`src/planetfall/main.py:66-75`:** Injects synthetic failure flags (`odd_even_mismatch`, `secondary_eclipse`, `centroid_motion`) based on candidate TIC ID modulo arithmetic if `candidate.get('label') == 'False Positive'`.
- **`src/planetfall/validators/publication_readiness.py`, `vespa_fp_analysis.py`, `uncertainty_assault.py`:** Hardcoded conditional checks for TIC `88863718` (TOI-1196) and TIC `114018671` to artificially boost novelty or suppress false-alarm probabilities.

---

## 3. Preserving TOI-1196 (TIC 88863718) as a Validation Case

In the original repository, TIC 88863718 was treated with special favoritism, hardcoding it to 'Optimistic Habitable Zone' with an artificially boosted novelty score of 95. TOI-1196 is a well-known TESS Object of Interest. In this reconstruction:
1. All hardcoded branches for TIC 88863718 are purged.
2. TOI-1196 is preserved strictly as a known confirmed-candidate validation benchmark.
3. It will not be claimed as an original discovery of this pipeline.

---

## 4. Initial Test Baseline Reproducibility

The baseline test suite `tests/test_basic.py` was executed using `.venv/bin/pytest tests/`:  
- **Tests Collected:** 3  
- **Tests Passed:** 3  
- **Tests Failed:** 0  
- **Execution Time:** 9.37 seconds  
- **Scientific Verdict:** The 3 passing tests verify only that `__version__ == '0.1.0-alpha'` and that empty module classes can be imported. Zero scientific algorithms or calculations are tested.

---

## 5. Next Immediate Phase

Proceed to **Phase 1: Audit Scientific Integrity**, independently verifying each of the 20 findings in `audit-results/scientific_integrity_findings.md`, producing a formalized `reports/DEFECT_REGISTER.csv` and `reports/SCIENTIFIC_INTEGRITY_AUDIT.md`.