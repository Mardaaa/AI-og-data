import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_olivetti_faces

import warnings

warnings.filterwarnings('ignore')

# Set style
plt.style.use('classic')

def costumize(x):
    # use a gray background
    ax = plt.axes()
    ax.set_axisbelow(True)

    # draw solid white grid lines
    plt.grid(color='w', linestyle='solid')

    # hide axis spines
    for spine in ax.spines.values():
        spine.set_visible(False)
        
    # hide top and right ticks
    ax.xaxis.tick_bottom()
    ax.yaxis.tick_left()

    # lighten ticks and labels
    ax.tick_params(colors='gray', direction='out')
    for tick in ax.get_xticklabels():
        tick.set_color('gray')
    for tick in ax.get_yticklabels():
        tick.set_color('gray')
        
    # control face and edge color of histogram
    ax.hist(x, edgecolor='#E6E6E6', color='#EE6666')

    plt.show()

def hist_and_lines():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(['a', 'b', 'c'], loc='lower left')

    plt.show()

x = np.random.randn(1000)

def main():
    # costumize(x)

    IPython_default = plt.rcParams.copy()
    plt.rcParams.update(IPython_default)

    # hist_and_lines()
    with plt.style.context('dark_background'):
        hist_and_lines()


if __name__ == '__main__':
    main()