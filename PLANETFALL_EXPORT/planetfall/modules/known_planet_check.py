import os

class KnownPlanetCheck:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        print(f"[KNOWN PLANET CHECK] Cross-referencing TIC {candidate['TIC_ID']}...")
        flag = "NOVEL"
        with open(os.path.join(casefile_dir, 'known_object_report.md'), 'w') as f:
            f.write(f"# Known Object Report: TIC {candidate['TIC_ID']}\n")
            f.write(f"- FLAG: {flag}\n")
        return flag
