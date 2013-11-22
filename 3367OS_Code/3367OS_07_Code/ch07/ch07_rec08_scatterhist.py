import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def scatterhist(x, y, figsize=(8,8)):
    """
    Create simple scatter & histograms of data x, y inside given plot

    @param figsize: Figure size to create figure
    @type figsize: Tuple of two floats representing size in inches

    @param x: X axis data set
    @type x: np.array

    @param y: Y axis data set
    @type y: np.array
    """
    _, scatter_axes = plt.subplots(figsize=figsize)

    # the scatter plot:
    scatter_axes.scatter(x, y, alpha=0.5)
    scatter_axes.set_aspect(1.)

    divider = make_axes_locatable(scatter_axes)
    axes_hist_x = divider.append_axes(position="top", sharex=scatter_axes,
                                      size=1, pad=0.1)
    axes_hist_y = divider.append_axes(position="right", sharey=scatter_axes,
                                      size=1, pad=0.1)

    # compute bins accordingly
    binwidth = 0.25

    # global max value in both data sets
    xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
    # number of bins
    bincap = int(xymax / binwidth) * binwidth

    bins = np.arange(-bincap, bincap, binwidth)
    nx, binsx, _ = axes_hist_x.hist(x, bins=bins, histtype='stepfilled',
                     orientation='vertical')
    ny, binsy, _ = axes_hist_y.hist(y, bins=bins, histtype='stepfilled',
                     orientation='horizontal')

    tickstep = 50
    ticksmax = np.max([np.max(nx), np.max(ny)])
    xyticks = np.arange(0, ticksmax + tickstep, tickstep)

    # hide x and y ticklabels on histograms
    for tl in axes_hist_x.get_xticklabels():
        tl.set_visible(False)
    axes_hist_x.set_yticks(xyticks)

    for tl in axes_hist_y.get_yticklabels():
        tl.set_visible(False)
    axes_hist_y.set_xticks(xyticks)

    plt.show()


if __name__ == '__main__':
    # import the data
    from ch07_search_data import DATA
    d = DATA

    # Now let's generate random data for the same period
    d1 = np.random.random(365)
    assert len(d) == len(d1)

    # try with the random data
#     d = np.random.randn(1000)
#     d1 = np.random.randn(1000)

    scatterhist(d, d1)
