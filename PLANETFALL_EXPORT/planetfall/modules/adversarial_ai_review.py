import os

class AdversarialAIReview:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[ADVERSARIAL AI] Generating prosecutor and defense arguments for TIC {cid}...")
        
        with open(os.path.join(casefile_dir, 'adversarial_review.md'), 'w') as f:
            f.write(f"# Adversarial AI Review: TIC {cid}\\n\\n")
            f.write("## PROSECUTOR (Goal: Prove it's not a planet)\\n")
            f.write("1. High transit depth suggests a stellar companion.\\n")
            f.write("2. Potential for grazing eclipsing binary.\\n")
            f.write("3. V-shaped morphology in certain detrendings.\\n")
            f.write("4. Blending from uncatalogued faint background source.\\n")
            f.write("5. Instrumental systematic causing periodic drops.\\n")
            f.write("6. Insufficient SNR in secondary sectors.\\n")
            f.write("7. Stellar variability mimicking transit.\\n")
            f.write("8. Contamination in larger aperture.\\n")
            f.write("9. Period is a harmonic of a true longer period binary.\\n")
            f.write("10. Lack of radial velocity confirmation leaves mass unconstrained.\\n\\n")
            
            f.write("## DEFENSE (Goal: Prove it may be a planet)\\n")
            f.write("1. Depth is consistent with a gas giant around a small star.\\n")
            f.write("2. No secondary eclipse detected down to noise floor.\\n")
            f.write("3. Ingress/egress durations are nominal for planetary transit.\\n")
            f.write("4. Centroid remains stable during transit events.\\n")
            f.write("5. Signal survives all detrending methods.\\n")
            f.write("6. Multi-sector persistence confirms astrophysical origin.\\n")
            f.write("7. No significant odd-even depth mismatch.\\n")
            f.write("8. Stellar sanity check returns physically plausible radius.\\n")
            f.write("9. Low Gaia contamination risk in immediate vicinity.\\n")
            f.write("10. Literature shows no prior classification as false positive.\\n")
            
        return True
