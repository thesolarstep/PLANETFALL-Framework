# PLANETFALL

**An adversarial, falsification-driven scientific framework for exoplanet candidate validation.**

> "We built this because Source 382 lied to us."

PLANETFALL is a Python-based framework designed to aggressively eliminate false-positive exoplanet candidates through adversarial scientific validation. Unlike traditional pipelines that seek to maximize discoveries, PLANETFALL is built to maximize confidence by treating every candidate as "guilty" of being a false positive until proven otherwise.

---

## 🚀 Repository Details
- **Description**: Adversarial validation framework for exoplanets.
- **Author**: KADAM ADITYA ANIL (M.Sc. Microbiology, GATE XL Qualified, Nanobiotech Researcher)
- **ORCID**: [0000-0001-9585-8955](https://orcid.org/0000-0001-9585-8955)
- **Topics**: `astronomy`, `exoplanets`, `validation`, `scientific-software`, `adversarial-validation`, `python`

---

## 🧠 Scientific Motivation
The primary bottleneck in exoplanet research is not the lack of signals, but the abundance of astrophysical false positives (Eclipsing Binaries, background blends) and instrumental artifacts. PLANETFALL implements a "Prosecution Engine" that subjects signals to a battery of tests designed to break them.

## 🏛 Architecture Overview
- **Modular Engines**: Independent validation modules for signal integrity, binary checks, and stellar contamination.
- **The Tribunal**: A decision-making core that weighs evidence from all modules to issue a final verdict.
- **Automated Casefiles**: Detailed markdown reports and visualizations for every "prosecuted" candidate.

## 🛠 Installation
```bash
git clone https://github.com/thesolarstep/planetfall.git
cd planetfall
pip install -r requirements.txt
```

## 📖 Usage
```bash
python -m planetfall.main --data_dir path/to/your/data --out_dir ./output
```

## ⚖ Philosophy
PLANETFALL inherits the adversarial mindset of its predecessor, ANOMALY382. Its purpose is not to find new worlds, but to ensure that the worlds we claim to find actually exist. In our framework, a false negative is a statistic; a false positive is a failure.

## 🗺 Future Roadmap
- Integration with Gaia DR3 for enhanced contamination analysis.
- Advanced neural-adversarial review modules.
- Support for multi-sector TESS light curve reconstruction.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📜 Citation
If you use this software, please refer to [CITATION.md](CITATION.md).
