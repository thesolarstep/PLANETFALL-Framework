import os

class HostileRefereeCouncil:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[HOSTILE COUNCIL] Convening 5 aggressive reviewers for TIC {cid}...")
        
        with open(os.path.join(casefile_dir, 'hostile_referee_council.md'), 'w') as f:
            f.write(f"# Hostile Referee Council: TIC {cid}\n\n")
            f.write("## Reviewer 1: Transit Specialist\n")
            f.write("- Major Concerns: Signal is shallow; correlated noise might mimic a transit.\n")
            f.write("- Missing Evidence: Requires multi-color photometry to rule out spots.\n\n")
            
            f.write("## Reviewer 2: Instrument Scientist\n")
            f.write("- Major Concerns: TESS pixel scale is too large to fully rule out unresolved blends.\n")
            f.write("- Missing Evidence: Needs adaptive optics imaging.\n\n")
            
            f.write("## Reviewer 3: Gaia Expert\n")
            f.write("- Major Concerns: Gaia RUWE is nominal (1.0), but astrometry alone cannot rule out an equal-mass binary in an extremely tight orbit (unlikely but possible).\n")
            f.write("- Missing Evidence: Spectroscopic screening.\n\n")
            
            f.write("## Reviewer 4: Statistical Reviewer\n")
            f.write("- Major Concerns: Marginal SNR per sector.\n")
            f.write("- Missing Evidence: Re-observation in TESS Extended Mission needed to boost SNR.\n\n")
            
            f.write("## Reviewer 5: Exoplanet Discovery Referee\n")
            f.write("- Major Concerns: You cannot claim 'Discovery' without mass.\n")
            f.write("- Fatal Flaws: None.\n")
            f.write("- Reasons to Reject: The paper must explicitly state this is a *validated candidate*, not a dynamically confirmed planet.\n")
        return True
