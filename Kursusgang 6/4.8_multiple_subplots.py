import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import warnings

warnings.filterwarnings('ignore')

# Set style
plt.style.use('classic')

def subplots_by_hand():
    # ax1 = plt.axes()  # standard axes
    # ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])


    fig = plt.figure()
    ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4],
                    xticklabels=[], ylim=(-1.2, 1.2))
    ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4],
                    ylim=(-1.2, 1.2))

    x = np.linspace(0, 10)
    ax1.plot(np.sin(x))
    ax2.plot(np.cos(x))
    plt.show()

def simple_grids_of_subplots():
    fig = plt.figure()
    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    for i in range(1, 7):
        ax = fig.add_subplot(2, 3, i)
        ax.text(0.5, 0.5, str((2, 3, i)),
            fontsize=18, ha='center')
    plt.show()

def main():
    # subplots_by_hand()
    simple_grids_of_subplots()


if __name__ == '__main__':
    main()