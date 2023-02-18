import os
import pandas as pd

from CORAL import FloatingPipeline, GlobalManager
from ORBIT.core.library import initialize_library
import matplotlib.pyplot as plt
import datetime as dt
initialize_library("library")

from helpers import allocations
from plot_routines import plot_gantt

# Configure scenarios and keep_inputs
projects = "library/pipeline/wc-pipeline.xlsx"
scenarios = ['baseline', 'expanded']
base = "base.yaml"
library_path = "library"
savedir = "results"


if __name__ == '__main__':
    for s in scenarios:
        pipeline = FloatingPipeline(projects, base, sheet_name=s)
        manager = GlobalManager(pipeline.configs, allocations[s], library_path=library_path)
        manager.run()

        # Plot and save results
        df = pd.DataFrame(manager.logs).iloc[::-1]
        df = df.reset_index(drop=True).reset_index()

        port_map = pipeline.projects[["name", "associated_port"]].set_index("name").to_dict()['associated_port']
        df['port'] = [port_map[name] for name in df['name']]

        # savefig = savedir + '/s' + '_gantt'
        filename = str(s) + '_gantt'
        savefig = os.path.join(os.getcwd(), savedir, filename)
        plot_gantt(df, manager, fname=savefig)
