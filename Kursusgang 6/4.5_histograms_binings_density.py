import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

# Set style
plt.style.use('seaborn-v0_8-white')

def plot_histogram(data, num_histograms=3):
    if num_histograms == 1:
        plt.hist(data, bins=30, alpha=0.5,
            histtype='stepfilled', color='steelblue',
            edgecolor='none')
    elif num_histograms == 3:
        x1 = np.random.normal(0, 0.8, 1000)
        x2 = np.random.normal(-2, 1, 1000)
        x3 = np.random.normal(3, 2, 1000)

        kwargs = dict(histtype='stepfilled', alpha=0.3, bins=40)

        plt.hist(x1, **kwargs)
        plt.hist(x2, **kwargs)
        plt.hist(x3, **kwargs)

    plt.show()

def two_dimensional_histograms_binnings(x, y, style='hist2d'):
    if style=='hist2d':
        plt.hist2d(x, y, bins=30, cmap='Blues')
        cb = plt.colorbar()
        cb.set_label('counts in bin')
    elif style =='hexbin':
        plt.hexbin(x, y, gridsize=30, cmap='Blues')
        cb = plt.colorbar(label='count in bin')

    plt.show()


def kernel_density_estimation(x, y):
    # fit an array of size [Ndim, Nsamples]
    data = np.vstack([x, y])
    kde = gaussian_kde(data)

    # evaluate on a regular grid
    xgrid = np.linspace(-3.5, 3.5, 40)
    ygrid = np.linspace(-6, 6, 40)
    Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
    Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

    # Plot the result as an image
    plt.imshow(Z.reshape(Xgrid.shape),
            origin='lower', aspect='auto',
            extent=[-3.5, 3.5, -6, 6],
            cmap='Blues')
    cb = plt.colorbar()
    cb.set_label("density")

    plt.show()

data = np.random.randn(1000)
mean = [0, 0]
cov = [[1, 1], [1, 2]]

x, y = np.random.multivariate_normal(mean, cov, 10000).T

def main():
    # plot_histogram(data, num_histograms=3)
    # two_dimensional_histograms_binnings(x, y, style='hexbin')
    kernel_density_estimation(x, y)

if __name__ == '__main__':
    main()