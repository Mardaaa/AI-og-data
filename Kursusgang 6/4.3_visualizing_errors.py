import matplotlib.pyplot as plt
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

def plot_basic_errorbars(x,dy,y, style='simple'):
    # Control appearance of lines and points using fmt-parameter
    if style == 'simple':
        plt.errorbar(x, y, yerr=dy, fmt='.k')
    if style == 'advanced':
        plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
                     ecolor='lightgray', elinewidth=3, capsize=0)
    plt.show()

def continuous_errors():
    # define the model and draw some data
    model = lambda x: x * np.sin(x)
    xdata = np.array([1, 3, 5, 6, 8])
    ydata = model(xdata)

    # Define the kernel
    kernel = C(1.0, (1e-4, 1e2)) * RBF(1.0, (1e-4, 1e2))

    # Compute the Gaussian process fit
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
    gp.fit(xdata[:, np.newaxis], ydata)

    xfit = np.linspace(0, 10, 1000)
    yfit, MSE = gp.predict(xfit[:, np.newaxis], return_std=True)
    dyfit = 2 * np.sqrt(MSE)  # 2*sigma ~ 95% confidence region

    # Visualize result
    plt.plot(xdata, ydata, 'or')
    plt.plot(xfit, yfit, '-', color='gray')
    
    plt.fill_between(xfit, yfit-dyfit, yfit+dyfit,
                     color='gray', alpha=0.2)
    plt.xlim(0, 10)
    
    # Show plot
    plt.show()


x = np.linspace(0,10,50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)
def main():
    # plot_basic_errorbars(x, dy, y, style='advanced')
    continuous_errors()

if __name__ == '__main__':
    main()