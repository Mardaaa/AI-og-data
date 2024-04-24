import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

# Set style
plt.style.use('seaborn-v0_8-whitegrid')


def scatter_plot_with_plt_plot(x, y):
    plt.plot(x, y, 'o',color='black')
    plt.show()

def scatter_plot_with_scatter(x, y, scatter='simple'):
    if scatter == 'simple':
        plt.scatter(x,y, marker='o')
    
    elif scatter == 'random':
        rng = np.random.RandomState(0)
        x = rng.randn(100)
        y = rng.randn(100)
        colors = rng.rand(100)
        sizes = 1000 * rng.rand(100)

        plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
                    cmap='viridis')
        plt.colorbar() # Show color scale
    elif scatter == 'iris':
        iris = load_iris()
        features = iris.data.T

        plt.scatter(features[0], features[1], alpha=0.2,
                    s=100*features[3], c=iris.target, cmap='viridis')
        plt.xlabel(iris.feature_names[0])
        plt.ylabel(iris.feature_names[1])

    plt.show()

x = np.linspace(0,10,30)
y = np.sin(x)
def main():
    # scatter_plot_with_plt_plot(x, y)
    scatter_plot_with_scatter(x,y, scatter='iris')


if __name__ == '__main__':
    main()