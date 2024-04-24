import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits import mplot3d
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')

# Set style
plt.style.use('classic')

def simple_plot(x, y):
    plt.plot(x, y)
    plt.legend('ABCDEF', ncol=2, loc='upper left')

    plt.show()

def plot_histograms_etc():
    data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
    data = pd.DataFrame(data, columns=['x', 'y'])

    for col in 'xy':
        sns.kdeplot(data[col], shade=True)
        sns.distplot(data['x'])
        sns.distplot(data['y'])

    plt.show()

# Create some data
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)

def main():
    sns.set()
    # simple_plot(x,y)
    plot_histograms_etc()



if __name__ == '__main__':
    main()