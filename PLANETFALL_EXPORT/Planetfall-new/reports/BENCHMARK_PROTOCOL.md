# OPERATION PLANETFALL: Independent Benchmark Protocol

**Document Version:** 1.0.0  
**Status:** APPROVED & EXECUTED  
**Author:** Antigravity Autonomous Scientific Verification Team  
**Date:** 2026-10-25  

---

## 1. Benchmarking Philosophy & Governance

Rather than relying on a single aggregate metric or synthetic test cases, OPERATION PLANETFALL establishes eight complementary benchmarks evaluating every stage of exoplanet discovery and validation:

1. **Benchmark 1: Confirmed-Planet Blind Recovery**  
   Evaluates discovery engine completeness on known confirmed transiting exoplanets observed by NASA's TESS mission without supplying known periods, epochs, or dispositions.
2. **Benchmark 2: False-Positive Rejection**  
   Evaluates the adversarial vetting gauntlet on documented eclipsing binaries and self-luminous companions, measuring specificity, false alarm rates, and Bayesian false positive probabilities.
3. **Benchmark 3: Authentic Injection-Recovery**  
   Injects synthetic limb-darkened Mandel-Agol transits across a 2D parameter grid of periods and depths into genuine observational light curves to measure empirical completeness and parameter bias.
4. **Benchmark 4: Blind-Search Evaluation on Held-Out Targets**  
   Evaluates the frozen pipeline on held-out target light curves without access to reference catalogs or labels, revealing reference answers only after predictions are finalized.
5. **Benchmark 5: Detrending Robustness & Stability**  
   Compares Tukey's biweight window filter, running median filter, and cubic spline detrending on identical time series to measure out-of-transit continuum RMS and transit preservation.
6. **Benchmark 6: Contamination & Centroid Resolution Analysis**  
   Measures photocenter centroid shifts between in-transit and out-of-transit difference images on TESS Target Pixel Files (TPF) and verifies honest handling of missing pixel data.
7. **Benchmark 7: Cross-Sector Repeatability**  
   Tests consistency of period, transit depth, and SNR across independent observing sectors (e.g. Sector 2 vs Sector 3).
8. **Benchmark 8: Adversarial Regression Suite**  
   Prosecutes edge cases including 1-day diurnal sampling aliases, non-finite input data (NaN/Inf), unphysical planetary radii (> 2.5 R_jup), and checks for absolute immunity to ground-truth label leakage.

---

## 2. Quantitative Metrics & Formulas

- **Period Relative Error:** $\epsilon_P = \frac{|P_{recovered} - P_{ref}|}{P_{ref}}$
- **Transit Signal-to-Noise Ratio (SNR):** $SNR = \frac{\delta}{\sigma_{eff}} \sqrt{N_{in}}$
- **Signal Detection Efficiency (SDE):** $SDE = \frac{Power_{max} - \mu_{power}}{\sigma_{power}}$
- **Odd-Even Z-score:** $Z_{oe} = \frac{|\delta_{odd} - \delta_{even}|}{\sqrt{\sigma_{odd}^2 + \sigma_{even}^2}}$
- **Secondary Eclipse Significance:** $SNR_{sec} = \frac{\delta_{sec}}{\sigma_{sec}}$
- **Centroid Offset:** $\Delta r = \sqrt{(\bar{x}_{diff} - \bar{x}_{out})^2 + (\bar{y}_{diff} - \bar{y}_{out})^2}$ in TESS pixels (scale: 21 arcsec / pixel)
- **Bayesian False Positive Probability (FPP):**
  $$P(\text{FP} \mid D) = \frac{P(D \mid \text{FP}) P(\text{FP})}{P(D \mid \text{FP}) P(\text{FP}) + P(D \mid \text{Planet}) P(\text{Planet})}$$
