import matplotlib.cm as cm
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.text as txt
import matplotlib.patches as mpatches
import os
import datetime as dt
import pandas as pd

from CORAL.utils import get_installed_capacity_by


def mysave(fig, froot, mode='png'):
    assert mode in ['png', 'eps', 'pdf', 'all']
    fileName, fileExtension = os.path.splitext(froot)
    padding = 0.1
    dpiVal = 200
    legs = []
    for a in fig.get_axes():
        addLeg = a.get_legend()
        if not addLeg is None: legs.append(a.get_legend())
    ext = []
    if mode == 'png' or mode == 'all':
        ext.append('png')
    if mode == 'eps':  # or mode == 'all':
        ext.append('eps')
    if mode == 'pdf' or mode == 'all':
        ext.append('pdf')

    for sfx in ext:
        fig.savefig(fileName + '.' + sfx, format=sfx, pad_inches=padding, bbox_inches='tight',
                    dpi=dpiVal, bbox_extra_artists=legs)


titleSize = 24  # 40 #38
axLabelSize = 20  # 38 #36
tickLabelSize = 18  # 30 #28
ganttTick = 18
legendSize = tickLabelSize + 2
textSize = legendSize - 2
deltaShow = 4
linewidth = 3


def myformat(ax, linewidth=linewidth, xticklabel=tickLabelSize, yticklabel=tickLabelSize, mode='save'):
    assert type(mode) == type('')
    assert mode.lower() in ['save', 'show'], 'Unknown mode'

    def myformat(myax, linewidth=linewidth, xticklabel=xticklabel, yticklabel=yticklabel):
        if mode.lower() == 'show':
            for i in myax.get_children():  # Gets EVERYTHING!
                if isinstance(i, txt.Text):
                    i.set_size(textSize + 3 * deltaShow)

            for i in myax.get_lines():
                if i.get_marker() == 'D': continue  # Don't modify baseline diamond
                i.set_linewidth(linewidth)
                # i.set_markeredgewidth(4)
                i.set_markersize(10)

            leg = myax.get_legend()
            if not leg is None:
                for t in leg.get_texts(): t.set_fontsize(legendSize + deltaShow + 6)
                th = leg.get_title()
                if not th is None:
                    th.set_fontsize(legendSize + deltaShow + 6)

            myax.set_title(myax.get_title(), size=titleSize + deltaShow, weight='bold', pad=20)
            myax.set_xlabel(myax.get_xlabel(), size=axLabelSize + deltaShow, weight='bold')
            myax.set_ylabel(myax.get_ylabel(), size=axLabelSize + deltaShow, weight='bold')
            myax.tick_params(labelsize=tickLabelSize + deltaShow)
            myax.patch.set_linewidth(3)
            for i in myax.get_xticklabels():
                i.set_size(tickLabelSize + deltaShow)
            for i in myax.get_xticklines():
                i.set_linewidth(3)
            for i in myax.get_yticklabels():
                i.set_size(yticklabel + deltaShow)
            for i in myax.get_yticklines():
                i.set_linewidth(3)

        elif mode.lower() == 'save':
            for i in myax.get_children():  # Gets EVERYTHING!
                if isinstance(i, txt.Text):
                    i.set_size(textSize)

            for i in myax.get_lines():
                if i.get_marker() == 'D': continue  # Don't modify baseline diamond
                i.set_linewidth(linewidth)
                # i.set_markeredgewidth(4)
                i.set_markersize(10)

            leg = myax.get_legend()
            if not leg is None:
                for t in leg.get_texts(): t.set_fontsize(legendSize)
                th = leg.get_title()
                if not th is None:
                    th.set_fontsize(legendSize)

            myax.set_title(myax.get_title(), size=titleSize, weight='bold', pad=20)
            myax.set_xlabel(myax.get_xlabel(), size=axLabelSize, weight='bold')
            myax.set_ylabel(myax.get_ylabel(), size=axLabelSize, weight='bold')
            myax.tick_params(labelsize=tickLabelSize)
            myax.patch.set_linewidth(3)
            for i in myax.get_xticklabels():
                i.set_size(xticklabel)
            for i in myax.get_xticklines():
                i.set_linewidth(3)
            for i in myax.get_yticklabels():
                i.set_size(yticklabel)
            for i in myax.get_yticklines():
                i.set_linewidth(3)

    if type(ax) == type([]):
        for i in ax: myformat(i)
    else:
        myformat(ax)

def initFigAxis(figx=12, figy=9):
    fig = plt.figure(figsize=(figx, figy))
    ax = fig.add_subplot(111)
    return fig, ax

def plot_gantt(df, manager, fname=None):
    fig, ax = initFigAxis()

    df["Date Finished"].plot(kind="barh", ax=ax, zorder=4, label="Project Time", color="#b1b1b1")
    df["Date Started"].plot(kind="barh", color="#e9e9e9", ax=ax, zorder=4, label="Project Delay", hatch="////", linewidth=0.5)
    df["Date Initialized"].plot(kind='barh', ax=ax, zorder=4, label="__nolabel__", color='w')


    # Plot formatting
    ax.set_xlabel("")
    ax.set_ylabel("")
    _ = ax.set_yticklabels(df['name'])

    plt.yticks(fontsize=6)
    plt.plot((0, 0), (0, 30), scaley = False)
    ax.legend()
    ax.set_xlim(manager._start - dt.timedelta(days=30), dt.date(2060, 6, 1) + dt.timedelta(days=30))
    num_proj = len(df['Date Finished'])

    ax.axvline(dt.date(2031, 1, 1), lw=0.5, ls="--", color="#6400D3", zorder=6)
    installed_capacity_31 = get_installed_capacity_by(df, 2031)
    ax.text(x=dt.date(2051, 1, 1), y=25, s=f"Capacity installed \nby end of 2030: \n{installed_capacity_31/1000:,.3} GW", fontsize=20, color="#6400D3")

    ax.axvline(dt.date(2046, 1, 1), lw=0.5, ls="--", color="#008080", zorder=6)
    installed_capacity_46 = get_installed_capacity_by(df, 2046)
    ax.text(x=dt.date(2051, 1, 1), y=15, s=f"Capacity installed \nby end of 2045: \n{installed_capacity_46/1000:,.3} GW", fontsize=20, color="#008080")

    fig.subplots_adjust(left=0.25)


    if fname is not None:
        myformat(ax)
        mysave(fig, fname)
        plt.close()

## Bar chart of annual throughput of each port
def plot_throughput(throughput, fname=None):
    fig, ax = initFigAxis()

    throughput.plot.bar(ax=ax, width=0.75)

    ax.set_ylim(0, 2000)

    ax.set_ylabel("Annual Capacity Throughput (MW)")
    ax.set_xlabel("")

    plt.xticks(rotation=0, fontsize=6)
    plt.yticks(fontsize=6)

    ax.legend(fontsize=6, ncol=5)

    if fname is not None:
        myformat(ax)
        mysave(fig, fname)
        plt.close()
    #fname_t = 'results/throughput_'+str(s)+'.png'
    #fig.savefig(fname_t, dpi=300)

## Plot a near-term gantt chart
def plot_gantt_nt(df, manager, num_proj, fname=None):
    fig, ax = initFigAxis()

    df_nt = pd.DataFrame()
    for i in range(1, num_proj+1):
        row = df.loc[df['name'] == 'Project ' + str(i)]
        df_nt = pd.concat([df_nt, row])

    df_nt["Date Finished"].plot(kind="barh", ax=ax, zorder=4, label="Project Time", color="#b1b1b1")
    df_nt["Date Started"].plot(kind="barh", color="#e9e9e9", ax=ax, zorder=4, label="Project Delay", hatch="////", linewidth=0.5)
    df_nt["Date Initialized"].plot(kind='barh', ax=ax, zorder=4, label="__nolabel__", color='w')

    # Plot formatting
    ax.set_xlabel("")
    ax.set_ylabel("")
    _ = ax.set_yticklabels(df_nt['region'])

    plt.yticks(fontsize=6)
    plt.plot((0, 0), (0, 30), scaley = False)
    ax.legend()
    ax.set_xlim(manager._start - dt.timedelta(days=30), dt.date(2040, 6, 1) + dt.timedelta(days=30))

    ax.axvline(dt.date(2031, 1, 1), lw=0.5, ls="--", color="#6400D3", zorder=6)
    installed_capacity_31 = get_installed_capacity_by(df, 2031)
    ax.text(x=dt.date(2051, 1, 1), y=25, s=f"Capacity installed \nby end of 2030: \n{installed_capacity_31/1000:,.3} GW", fontsize=20, color="#6400D3")

    fig.subplots_adjust(left=0.25)

    if fname is not None:
        myformat(ax)
        mysave(fig, fname)
        plt.close()