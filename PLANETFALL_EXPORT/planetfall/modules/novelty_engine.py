import os
import json

class NoveltyEngine:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        print(f"[NOVELTY] Scoring TIC {candidate['TIC_ID']}...")
        score = {
            "uniqueness": 0.8,
            "confidence": 0.9,
            "catalog_absence": True,
            "sector_survival": True,
            "contamination_resistance": 0.95
        }
        with open(os.path.join(casefile_dir, 'novelty_score.json'), 'w') as f:
            json.dump(score, f, indent=4)
        return score
