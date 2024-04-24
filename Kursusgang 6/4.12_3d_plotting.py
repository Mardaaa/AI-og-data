import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d

import warnings

warnings.filterwarnings('ignore')

# Set style
plt.style.use('classic')

def three_dimensional_axis():
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    plt.show()

def three_dimensional_points_and_lines():
    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')

    # Data for three-dimensional scattered points
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')

    plt.show()

def main():
    # three_dimensional_axis()
    three_dimensional_points_and_lines()



if __name__ == '__main__':
    main()