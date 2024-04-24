import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid')

def f(x,y):
    return np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

def visualizing_3d_function(X, Y, Z, fill='no'):
    if fill == 'no':
        plt.contour(X, Y, Z, 20, cmap='RdGy')
    elif fill == 'yes':
        plt.contourf(X, Y, Z, 20, cmap='RdGy')
        plt.colorbar()

        plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
           cmap='RdGy')
    elif fill == 'combine':
        contours = plt.contour(X, Y, Z, 3, colors='black')
        plt.clabel(contours, inline=True, fontsize=8)

        plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower',
                cmap='RdGy', alpha=0.5)
        plt.colorbar()
    plt.show()

x = np.linspace(0,5,50)
y = np.linspace(0,5,40)

X, Y = np.meshgrid(x,y)
def main():
    Z = f(X,Y)
    visualizing_3d_function(X, Y, Z, fill='combine')

if __name__ == '__main__':
    main()