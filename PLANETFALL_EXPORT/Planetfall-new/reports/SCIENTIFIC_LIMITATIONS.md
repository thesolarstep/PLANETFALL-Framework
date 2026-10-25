# Scientific Limitations & Physical Operational Boundaries

**Framework:** OPERATION PLANETFALL  
**Version:** 1.0.0  
**Scope:** Observational Photometry, False-Positive Discrimination, and Candidate Validation  

---

## 1. Photometric and Temporal Limits

1. **Transit Depth and Host Star Brightness:**
   - On bright TESS targets ($T_{mag} < 10$), the 2-minute cadence SPOC light curves achieve CDPP $\approx 100-300$ ppm. The detection threshold for reliable blind recovery ($SNR \ge 7.0$) is approximately $\delta \ge 500$ ppm (sub-Neptune / Neptune radius).
   - For faint stars ($T_{mag} > 13$), high photometric scatter restricts detection to Jovian transits ($\delta \ge 3,000$ ppm). Earth-sized planets around solar-type stars ($\delta \approx 84$ ppm) cannot be detected in single-sector TESS data without multi-year co-addition.

2. **Orbital Baseline and Sector Duration:**
   - A single TESS observing sector spans $\approx 27.4$ days.
   - To satisfy the minimum requirement of 2 observed transits, the maximum blind search period in a single sector is $P \le 13.5$ days.
   - For orbital periods $P > 13.5$ days, multi-sector stitched photometry is required.

---

## 2. Spatial and Pixel Resolution Limits

1. **TESS Pixel Scale (21 arcsec / pixel):**
   - TESS has large $21'' \times 21''$ pixels. The photometric aperture often spans multiple pixels ($1-2$ arcminutes), encompassing multiple background stars.
   - While difference-image centroiding can resolve photocenter shifts $> 0.5$ pixels ($\approx 10$ arcsec), blended sources closer than $2-3$ arcsec cannot be resolved photometrically.
   - Ground-based high-resolution adaptive optics or speckle imaging is required to rule out sub-arcsecond bound stellar companions.

---

## 3. Astrophysical False Positive Degeneracies

1. **Grazing Eclipsing Binaries:**
   - A grazing stellar binary where only the limb of the secondary grazes the primary can produce a shallow V-shaped transit profile mimicking a large gas giant.
   - If the signal-to-noise ratio is insufficient to distinguish the flat-bottomed Mandel-Agol profile from a V-shape, the candidate must remain `UNRESOLVED_AMBIGUOUS` until radial velocity measurements can constrain companion mass.

2. **Circular Orbit Assumption:**
   - The secondary eclipse search evaluates phase $\phi \approx 0.5$. In highly eccentric orbits ($e > 0.3$), the secondary eclipse shifts away from phase 0.5 and may be missed if broad phase searches are not conducted.
