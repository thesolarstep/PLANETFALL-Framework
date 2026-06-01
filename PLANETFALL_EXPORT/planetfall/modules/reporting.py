import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class ReportingEngine:
    def __init__(self, out_dir):
        self.out_dir = out_dir

    def prepare_casefile(self, candidate):
        cid = candidate['TIC_ID']
        casefile_dir = os.path.join(self.out_dir, f'casefile_{cid}')
        os.makedirs(casefile_dir, exist_ok=True)
        return casefile_dir

    def mock_plots(self, casefile_dir):
        fig, ax = plt.subplots()
        ax.plot([0, 1], [0, 1])
        fig.savefig(os.path.join(casefile_dir, 'lightcurve.png'))
        fig.savefig(os.path.join(casefile_dir, 'folded_lightcurve.png'))
        fig.savefig(os.path.join(casefile_dir, 'periodogram.png'))
        plt.close(fig)

    def generate_clown(self):
        clown = """
          _,,,,_
        /       \\
       |  o   o  |
       |  .---.  |
        \\ \\___/ /
         '-----'
         CLOWNED

No genuine discoveries. Every "anomaly" was successfully destroyed by rigorous statistical testing. 
The field consists entirely of known stars, faint catalog omissions, and detector noise.

The framework's purpose is to destroy false planets.
This is a success condition.
"""
        with open(os.path.join(self.out_dir, 'clown.md'), 'w') as f:
            f.write(clown)
