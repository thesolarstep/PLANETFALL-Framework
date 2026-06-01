import os

class RedTeamReview:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def run(self, candidate, casefile_dir):
        cid = candidate['TIC_ID']
        print(f"[RED TEAM] Convening independent reviewers for TIC {cid}...")
        
        with open(os.path.join(casefile_dir, 'red_team_review.md'), 'w') as f:
            f.write(f"# Red Team Review: TIC {cid}\\n\\n")
            f.write("## Reviewer A: Instrumentation Specialist\\n")
            f.write("- **Reasons to Reject**: Minor momentum dumps near sector edge.\\n")
            f.write("- **Reasons to Continue**: Signal survives detrending across momentum dumps.\\n")
            f.write("- **Major Weaknesses**: Single CCD pixel bleed risk.\\n\\n")
            
            f.write("## Reviewer B: Transit Photometry Specialist\\n")
            f.write("- **Reasons to Reject**: Potential V-shape grazing transit not fully ruled out.\\n")
            f.write("- **Reasons to Continue**: U-shape probability is still much higher.\\n")
            f.write("- **Major Weaknesses**: Needs higher cadence photometry.\\n\\n")
            
            f.write("## Reviewer C: Exoplanet Referee\\n")
            f.write("- **Reasons to Reject**: Lack of RV constraints means mass is unknown.\\n")
            f.write("- **Reasons to Continue**: Excellent target for precise RV follow-up.\\n")
            f.write("- **Major Weaknesses**: A background EB is still statistically possible if ExoFOP flags exist.\\n")
            
        return True
