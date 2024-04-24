import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

""" Chapter 4: Introduction """
# Set style
plt.style.use('classic')

def plotting_from_a_script(line='dashed', save='y'):
    ### Plotting from a script
    x = np.linspace(0,10,100)
    if line == 'dashed':
        plt.plot(x, np.sin(x), '-')
        plt.plot(x, np.cos(x), '--')
    else:
        plt.plot(x, np.sin(x))
        plt.plot(x, np.cos(x))
    
    # if save == 'y':
        # fig.savefig('my_figure.png')

    plt.show()

def object_oriented_interface(x):
    # create a grid of plots
    # ax will be an array of two Axes objects
    fig, ax = plt.subplots(2)

    # Call plot() method on the appropriate object
    ax[0].plot(x, np.sin(x))
    ax[1].plot(x, np.cos(x))

    plt.show()

x = np.linspace(0,10,100)
def main():
    # Plotting from a script
    # plotting_from_a_script('dashed')

    # Object oriented
    object_oriented_interface(x)



if __name__ == '__main__':
    main()
