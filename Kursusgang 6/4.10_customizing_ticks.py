import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_olivetti_faces

import warnings

warnings.filterwarnings('ignore')

# Set style
plt.style.use('classic')

def hiding_ticks_or_labels():
    ax = plt.axes(xscale='log', yscale='log')
    ax.grid()

    ax = plt.axes()
    ax.plot(np.random.rand(50))

    ax.yaxis.set_major_locator(plt.NullLocator())
    ax.xaxis.set_major_formatter(plt.NullFormatter())

    plt.show()

def face_data():
    # Get some face data from scikit-learn
    faces = fetch_olivetti_faces().images

    fig, ax = plt.subplots(5, 5, figsize=(5, 5))
    fig.subplots_adjust(hspace=0, wspace=0)

    for i in range(5):
        for j in range(5):
            ax[i, j].xaxis.set_major_locator(plt.NullLocator())
            ax[i, j].yaxis.set_major_locator(plt.NullLocator())
            ax[i, j].imshow(faces[10 * i + j], cmap="bone")

    plt.show()

def main():
    # hiding_ticks_or_labels()
    face_data()

if __name__ == '__main__':
    main()