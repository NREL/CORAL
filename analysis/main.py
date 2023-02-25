import os
import pandas as pd
import numpy as np

from CORAL import FloatingPipeline, GlobalManager
from CORAL.utils import get_installed_capacity_by
from ORBIT.core.library import initialize_library
import matplotlib.pyplot as plt
import datetime as dt
initialize_library("library")

from helpers import allocations, future_allocations
from plot_routines import plot_gantt, plot_throughput, plot_gantt_nt

# Configure scenarios and keep_inputs
projects = "library/pipeline/wc-pipeline.xlsx"
scenarios = ['Baseline-limited-ports', 'Baseline-South-CA', 'Baseline-Central-CA', 'Expanded-all-ports']
# scenarios = ['Baseline-limited-ports']
base = "base.yaml"
library_path = "library"
weather_path = "library/weather/humboldt_weather_2010_2018.csv"
savedir = "results"

writer = pd.ExcelWriter("results/cumulative-capacity.xlsx")

if __name__ == '__main__':

    weather = pd.read_csv(weather_path, parse_dates=["datetime"]).set_index("datetime")
    weather_long = pd.concat([weather]*6) # Need a 50+ year time series for limited port scenario (should be the longest)

    for s in scenarios:
        pipeline = FloatingPipeline(projects, base, sheet_name=s)
        manager = GlobalManager(pipeline.configs, allocations[s], library_path=library_path, weather=weather_long)

        # Check (and add) any port or vessel resources that are not online at the start of the simulatino
        for s_fa,v in future_allocations.items():
            if s_fa == s:
                for vi in v:
                    manager.add_future_resources(vi[0], vi[1], vi[2])

        manager.run()

        # Plot and save results, assign ports to projects
        df = pd.DataFrame(manager.logs).iloc[::-1]
        df = df.reset_index(drop=True).reset_index()

        port_map = pipeline.projects[["name", "associated_port", "capacity"]].set_index("name").to_dict()['associated_port']
        df['port'] = [port_map[name] for name in df['name']]

        region_map = pipeline.projects[["name", "reference_site_location"]].set_index("name").to_dict()['reference_site_location']
        df['region'] = [region_map[name] for name in df['name']]

        capacity_map = pipeline.projects[["name", "capacity"]].set_index("name").to_dict()['capacity']
        df['capacity'] = [capacity_map[name] for name in df['name']]

        # savefig = savedir + '/s' + '_gantt'
        filename = str(s) + '_gantt'
        savefig = os.path.join(os.getcwd(), savedir, filename)
        plot_gantt(df, manager, fname=savefig)

        # Plot first five projects:
        filename_nt = str(s) + '_nt_gantt'
        savefig_nt = os.path.join(os.getcwd(), savedir, filename_nt)
        first_projs = 5
        plot_gantt_nt(df, manager, first_projs, fname=savefig_nt)

        # create a .csv file with cummulative installed capacities
        df['finish-year'] = pd.DatetimeIndex(df['Date Finished']).year

        minyear = df['finish-year'].min()
        maxyear = df['finish-year'].max()
        all_years = list(range(minyear, maxyear+1))
        annual_cap = []
        for year in all_years:
            installed_capacity = get_installed_capacity_by(df, year)
            annual_cap.append(installed_capacity)
        caps = pd.DataFrame(list(zip(all_years, annual_cap)), columns =['Year', 'Cummulative Installed Capacity'])
        caps.to_excel(writer, sheet_name=str(s), index=False)

        # Annual throughput
        res = []

        for _, project in df.iterrows():

            if project["Date Finished"].year == project["Date Started"].year:
                res.append((project["Date Finished"].year, project["port"], project["capacity"]))

            else:

                total = project["Date Finished"].date() - project["Date Started"].date()
                for year in np.arange(project["Date Started"].year, project["Date Finished"].year + 1):
                    if year == project["Date Started"].year:
                        perc = (dt.date(year + 1, 1, 1) - project["Date Started"].date()) / total

                    elif year == project["Date Finished"].year:
                        perc = (project["Date Finished"].date() - dt.date(year, 1, 1)) / total

                    else:
                        perc = (dt.date(year + 1, 1, 1) - dt.date(year, 1, 1)) / total

                    res.append((year, project["port"], perc * project["capacity"]))

        throughput = pd.DataFrame(res, columns=["year", "port", "capacity"]).pivot_table(
            index=["year"],
            columns=["port"],
            aggfunc="sum",
            fill_value=0.
        )["capacity"]

        # Plot throughput
        filename_thp = str(s) + '_throughput'
        savefig = os.path.join(os.getcwd(), savedir, filename_thp)
        plot_throughput(throughput, fname=savefig)


writer.close()