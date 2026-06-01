import os

class RefereePanel:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[HOSTILE REFEREES] Convening 5 hostile reviewers for TIC {cid}...")
        
        with open(os.path.join(casefile_dir, 'hostile_referee_panel.md'), 'w') as f:
            f.write(f"# Hostile Referee Panel: TIC {cid}\n\n")
            f.write("## Reviewer 1: Transit Specialist\n")
            f.write("- Reasons to reject: Limb darkening coefficients fixed instead of fitted.\n")
            f.write("- Evidence missing: Multi-color photometry to rule out spots.\n")
            f.write("- Required follow-up: Ground-based transit observation in different filter.\n\n")
            
            f.write("## Reviewer 2: Instrumentation Expert\n")
            f.write("- Reasons to reject: Possible systematic noise blending in TESS large pixels.\n")
            f.write("- Evidence missing: Sub-pixel centroid shift analysis at the millipixel level.\n")
            f.write("- Required follow-up: High-res speckle imaging.\n\n")
            
            f.write("## Reviewer 3: Gaia Expert\n")
            f.write("- Reasons to reject: Gaia RUWE is slightly elevated (1.15), suggesting possible unresolved binary.\n")
            f.write("- Evidence missing: Spectroscopic binary check.\n")
            f.write("- Required follow-up: High-resolution spectroscopy.\n\n")
            
            f.write("## Reviewer 4: Exoplanet Survey Scientist\n")
            f.write("- Reasons to reject: Candidate is just another TOI until mass is measured.\n")
            f.write("- Evidence missing: Mass constraints.\n")
            f.write("- Required follow-up: Precision Radial Velocity (PRV) campaign.\n\n")
            
            f.write("## Reviewer 5: Journal Referee\n")
            f.write("- Reasons to reject: The paper overclaims 'discovery'.\n")
            f.write("- Evidence missing: Tone down claims to 'validation'.\n")
            f.write("- Required follow-up: Address Reviewers 1-4 before resubmission.\n")
        return True
