import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Set style
plt.style.use('classic')

def costumize_legend(x):
    fig, ax = plt.subplots()
    ax.plot(x, np.sin(x), '-b', label='Sine')
    ax.plot(x, np.cos(x), '--r', label='Cosine')
    ax.axis('equal')
    # leg = ax.legend(loc='lower center', frameon=False, ncol=2)
    leg = ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)
    plt.show()


def choose_elements_for_legend(x):
    y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
    lines = plt.plot(x, y)

    # lines is a list of plt.Line2D instances
    # plt.legend(lines[:2], ['first', 'second'])

    plt.plot(x, y[:, 0], label='first')
    plt.plot(x, y[:, 1], label='second')
    plt.plot(x, y[:, 2:])
    plt.legend(framealpha=1, frameon=True)
    plt.show()


def multiple_legends(x):
    fig, ax = plt.subplots()

    lines = []
    styles = ['-', '--', '-.', ':']
    x = np.linspace(0, 10, 1000)

    for i in range(4):
        lines += ax.plot(x, np.sin(x - i * np.pi / 2),
                        styles[i], color='black')
    ax.axis('equal')

    # specify the lines and labels of the first legend
    ax.legend(lines[:2], ['line A', 'line B'],
            loc='upper right', frameon=False)

    # Create the second legend and add the artist manually.
    from matplotlib.legend import Legend
    leg = Legend(ax, lines[2:], ['line C', 'line D'],
                loc='lower right', frameon=False)
    ax.add_artist(leg)

    plt.show()


x = np.linspace(0, 10, 1000)
def main():
    # costumize_legend(x)
    # choose_elements_for_legend(x)
    multiple_legends(x)

if __name__ == '__main__':
    main()