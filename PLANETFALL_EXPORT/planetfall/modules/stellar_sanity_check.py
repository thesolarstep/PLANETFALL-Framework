import os

class StellarSanityCheck:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[STELLAR SANITY] Validating physical parameters for TIC {cid}...")
        
        # Mock logic based on Phase I results
        inferred_class = "JOVIAN"
        if candidate.get('depth', 0) > 0.10:
             inferred_class = "UNPHYSICAL"
        elif candidate.get('depth', 0) < 0.01:
             inferred_class = "SUPER_EARTH"
            
        with open(os.path.join(casefile_dir, 'stellar_sanity_report.md'), 'w') as f:
            f.write(f"# Stellar Sanity Check: TIC {cid}\\n")
            f.write("- Stellar radius: 1.0 Rsun (estimated)\\n")
            f.write("- Stellar temperature: 5700K (estimated)\\n")
            f.write(f"- Inferred planet class: {inferred_class}\\n")
            f.write(f"\\nVerdict: Does size make physical sense? {'Yes' if inferred_class != 'UNPHYSICAL' else 'No'}\\n")
            
        return inferred_class != "UNPHYSICAL"
