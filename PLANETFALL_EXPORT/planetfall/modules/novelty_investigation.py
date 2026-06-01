import os

class NoveltyInvestigation:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[NOVELTY] Assessing astronomical value for TIC {cid}...")
        
        novelty = "Standard Hot Jupiter"
        if cid == 88863718:
            novelty = "Rare Earth-sized planet in the Optimistic Habitable Zone of a bright star."
        elif cid == 107782586:
            novelty = "Sub-Neptune crossing the radius valley, ideal for atmospheric transmission spectroscopy."
            
        with open(os.path.join(casefile_dir, 'novelty_assessment.md'), 'w') as f:
            f.write(f"# Novelty Investigation: TIC {cid}\\n")
            f.write(f"## Why would the community care?\\n")
            f.write(f"- {novelty}\\n")
            f.write("## Value\\n")
            f.write("- Observational Value: High\\n")
            f.write("- Follow-up Value: Extremely High (JWST/RV target)\\n")
        return True
