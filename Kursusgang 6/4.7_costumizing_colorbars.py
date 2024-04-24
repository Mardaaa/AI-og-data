import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
import warnings

warnings.filterwarnings('ignore')

# Set style
plt.style.use('classic')




def plot_colorbar(I, cmap):
    plt.imshow(I, cmap=cmap)
    plt.colorbar()
    plt.show()

def color_limits_and_extensions(I):
    # make noise in 1% of the image pixels
    speckles = (np.random.random(I.shape) < 0.01)
    I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))

    plt.figure(figsize=(10, 3.5))

    plt.subplot(1, 2, 1)
    plt.imshow(I, cmap='RdBu')
    plt.colorbar()

    plt.subplot(1, 2, 2)
    plt.imshow(I, cmap='RdBu')
    plt.colorbar(extend='both')
    plt.clim(-1, 1)
    
    plt.show()

def discrete_color_bars(I):
    # make noise in 1% of the image pixels
    speckles = (np.random.random(I.shape) < 0.01)
    I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))
    
    plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
    plt.colorbar()
    plt.clim(-1, 1)

    plt.show()

x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])

def main():
    # plot_colorbar(I, cmap='gray')
    # color_limits_and_extensions(I)
    discrete_color_bars(I)
if __name__ == '__main__':
    main()