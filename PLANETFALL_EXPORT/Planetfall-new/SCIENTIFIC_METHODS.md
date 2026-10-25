# PLANETFALL: Scientific Methods and Mathematical Formulations

**Document Version:** 1.0.0  
**Author:** Antigravity Autonomous Scientific Team  
**Date:** 2026-10-25  

---

## 1. Photometric Conditioning and Preprocessing

### Quality Bitmasking
TESS 2-minute cadence light curves contain cadence-level quality flags. PLANETFALL applies a strict bitmask filtering out cadences contaminated by:
- Cosmic ray events in aperture (Bit 3, value 4)
- Spacecraft momentum dump / desaturation (Bit 6, value 32)
- Manual exclude flags (Bit 8, value 128)
- Severe Earth/Moon scattered light (Bit 11, value 1024)

### Outlier Rejection
To avoid corrupting transit dips while stripping positive flare contamination, PLANETFALL employs an asymmetric sigma-clipping protocol:
$$\text{MAD} = \text{median}(|f_i - \text{median}(f)|)$$
$$\sigma_{est} = 1.4826 \times \text{MAD}$$
Cadences with $f_i - 1.0 > 5.0 \times \sigma_{est}$ are clipped. Negative flux dips are explicitly protected from clipping to prevent signal attenuation.

---

## 2. Systematic Detrending: Windowed Tukey Biweight Filter

The gold standard for exoplanet detrending is Tukey's windowed biweight filter (window width $\tau = 0.5$ days). For points in window $|t_i - t_0| \le \tau/2$:
$$u_i = \frac{f_i - \text{median}(f)}{c \times 1.4826 \times \text{MAD}}, \quad c = 4.685$$
Weights:
$$w(u_i) = \begin{cases} (1 - u_i^2)^2 & \text{if } |u_i| < 1 \\ 0 & \text{otherwise} \end{cases}$$
The local trend estimator is:
$$\hat{f}_{trend}(t_0) = \frac{\sum w_i f_i}{\sum w_i}$$
Detrended flux is computed via continuum division: $f_{det}(t) = f(t) / \hat{f}_{trend}(t)$.

---

## 3. Blind Transit Discovery: Box Least Squares (BLS)

The Box Least Squares algorithm (Kovacs et al. 2002) searches over a grid of trial periods $P \in [P_{min}, P_{max}]$ and durations $q = T_{14} / P$:
$$SR(P, q) = \frac{s^2}{r (1 - r)}$$
where $r$ is the fraction of data in-transit, and $s$ is the weighted sum of flux residuals.

### Signal Detection Efficiency (SDE)
$$\text{SDE} = \frac{\max(Power) - \bar{P}}{\sigma_P}$$
A candidate requires $\text{SDE} \ge 6.0$ and $SNR \ge 7.0$ for confident detection.

### Alias and Harmonic Detection
- **1.0-day diurnal alias:** $|P - 1.00| \le 0.03$ days
- **0.5-day harmonic alias:** $|P - 0.50| \le 0.015$ days
- **Half-period harmonic:** Power at $P/2 \ge 0.85 \times Power(P)$
- **Double-period harmonic:** Power at $2P \ge 0.85 \times Power(P)$

---

## 4. Analytical Mandel-Agol Limb-Darkened Modeling

Phased transits are modeled using the Mandel & Agol (2002) quadratic limb-darkening profile:
$$I(\mu) = I_0 \left[ 1 - u_1 (1 - \mu) - u_2 (1 - \mu)^2 \right]$$
where $\mu = \cos \theta$, and $u_1, u_2$ are quadratic limb darkening coefficients.
The relative flux deficit $\Delta F(z, p)$ is computed as a function of normalized companion radius $p = R_p/R_*$ and projected center-to-center separation $z = d / R_*$.

### Least-Squares Optimization and Parameter Covariance
Model parameters $\mathbf{\theta} = [R_p/R_*, a/R_*, i, T_0]$ are optimized using Levenberg-Marquardt / bounded non-linear least squares.
The parameter covariance matrix is estimated from the Jacobian matrix $\mathbf{J}$:
$$\mathbf{Cov}(\mathbf{\theta}) = s^2 \left( \mathbf{J}^T \mathbf{J} \right)^{-1}, \quad s^2 = \frac{\chi^2}{N - K}$$
Parameter $1\sigma$ uncertainties are given by $\sigma_k = \sqrt{\mathbf{Cov}_{kk}}$.

---

## 5. Physical Parameter Derivation

1. **Planet Radius:**
   $$R_p = \left(\frac{R_p}{R_*}\right) R_* \quad (1 R_\odot = 109.076 R_\oplus = 9.731 R_{Jup})$$
   $$\left(\frac{\sigma_{R_p}}{R_p}\right)^2 = \left(\frac{\sigma_k}{k}\right)^2 + \left(\frac{\sigma_{R_*}}{R_*}\right)^2$$

2. **Semi-major Axis (Kepler's Third Law):**
   $$a = \left( \frac{G M_* P^2}{4 \pi^2} \right)^{1/3}$$

3. **Insolation Flux and Equilibrium Temperature:**
   $$S = \left(\frac{R_*}{a}\right)^2 \left(\frac{T_*}{5777 \text{ K}}\right)^4 S_\oplus$$
   $$T_{eq} = T_* \sqrt{\frac{R_*}{2a}} (1 - A_B)^{1/4}$$

---

## 6. Adversarial False-Positive Gauntlet

### Odd-Even Transit Depth Difference Test
$$Z_{oe} = \frac{|\delta_{odd} - \delta_{even}|}{\sqrt{\sigma_{odd}^2 + \sigma_{even}^2}}$$
A candidate is flagged as an Eclipsing Binary if $Z_{oe} \ge 3.5$ and $\frac{|\delta_{odd} - \delta_{even}|}{\max(\delta_{odd}, \delta_{even})} > 0.15$.

### Secondary Eclipse Test
Searches for flux deficits at phase $\phi \approx 0.5$:
$$SNR_{sec} = \frac{\delta_{sec}}{\sigma_{sec}}$$
Flagged as self-luminous / stellar companion if $SNR_{sec} \ge 3.5$ and $\delta_{sec} \ge 0.10 \times \delta_{pri}$.

### Centroid Difference-Image Photometry
$$\bar{x} = \frac{\sum x \cdot I(x, y)}{\sum I(x, y)}, \quad \bar{y} = \frac{\sum y \cdot I(x, y)}{\sum I(x, y)}$$
$$\Delta r = \sqrt{(\bar{x}_{diff} - \bar{x}_{out})^2 + (\bar{y}_{diff} - \bar{y}_{out})^2}$$
Flagged as background contaminant if $\Delta r > 1.0$ pixels ($> 21$ arcsec).
