import os

class ShapeForensics:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[SHAPE FORENSICS] Characterizing morphology for TIC {cid}...")
        
        # Mock logic
        morphology = "Planet-like"
        if candidate.get('depth', 0) > 0.05:
            morphology = "Ambiguous"
            
        with open(os.path.join(casefile_dir, 'shape_forensics.md'), 'w') as f:
            f.write(f"# Shape Forensics: TIC {cid}\\n")
            f.write("- Ingress duration: Nominal\\n")
            f.write("- Egress duration: Nominal\\n")
            f.write("- Symmetry: High\\n")
            f.write("- U-shape likelihood: High\\n")
            f.write("- V-shape likelihood: Low\\n")
            f.write(f"## Verdict\\n{morphology}\\n")
            
        return morphology in ["Planet-like", "Ambiguous"]
