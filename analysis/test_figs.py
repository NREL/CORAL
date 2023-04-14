import matplotlib.cm as cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.text as txt
import matplotlib.patches as mpatches
from matplotlib.patches import Patch
import os
import datetime as dt
import pandas as pd
import numpy as np

from CORAL.utils import get_installed_capacity_by

inv_path1 = 'library/investments/scenario-investments.xlsx'
inv_path2 = 'results/Baseline-Low_data.csv'

inv_df1 = pd.read_excel(inv_path1, sheet_name="schedule")
inv_df2 = pd.read_csv(inv_path2)

scenarios = ['Baseline-Low', 'Baseline-Mid (SC)', 'Baseline-Mid (CC)', 'Moderate-Low', 'Moderate-Mid (SC)', 'Expanded-High']
scenarios = ['Baseline-Low']

for s in scenarios:
    inv_date = inv_df2['Date Initialized'].values.tolist()
    agg_inv = inv_df2['investment'].values.tolist()

    fig = plt.figure(figsize=(6, 4))
    ax1 = fig.add_subplot(111)

    inv_df2.set_index('investment_year', inplace=True)

    #ax1.plot(inv_date, agg_inv)
    #inv_df2.set_index('Date Initialized')
    inv_df2['investment'].plot(ax=ax1, zorder=4)
    #ax1 = inv_df2.plot.line(x='index', y='investment')

    figsave = 'results/Summary Plots/' + s + '_inv.png'
    fig.savefig(figsave, bbox_inches='tight', dpi=300)
