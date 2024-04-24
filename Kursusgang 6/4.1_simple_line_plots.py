import matplotlib.pyplot as plt
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
# print(plt.style.available)

def simple_line_plots(x, num_lines=2):
    # Define figure
    fig = plt.figure()
    ax = plt.axes()

    if num_lines ==1:
        # Add curve
        ax.plot(x, np.sin(x))
    else:
        # Plot multiple lines
        plt.plot(x, np.sin(x))
        plt.plot(x, np.cos(x))

    plt.show()

def adjusting_line_colors_and_styles(x, adjustment='color'):
    # Define figure
    fig = plt.figure()
    ax = plt.axes()
    
    if adjustment == 'color':
        plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
        plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
        plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
        plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
        plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
        plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported
    elif adjustment == 'linestyle':
        plt.plot(x, x + 0, linestyle='solid')
        plt.plot(x, x + 1, linestyle='dashed')
        plt.plot(x, x + 2, linestyle='dashdot')
        plt.plot(x, x + 3, linestyle='dotted')

        plt.plot(x, x + 4, linestyle='-')  # solid
        plt.plot(x, x + 5, linestyle='--') # dashed
        plt.plot(x, x + 6, linestyle='-.') # dashdot
        plt.plot(x, x + 7, linestyle=':')  # dotted

    elif adjustment == 'both':
        plt.plot(x, x + 0, '-g')  # solid green
        plt.plot(x, x + 1, '--c') # dashed cyan
        plt.plot(x, x + 2, '-.k') # dashdot black
        plt.plot(x, x + 3, ':r');  # dotted red

    plt.show()

def adjusting_axes_limits(x, x_interval=(-1,11), y_interval=(-1.5,1.5), keyword='tight'):
    plt.plot(x, np.sin(x))
    x_start = x_interval[0]
    x_end = x_interval[1]

    y_start = y_interval[0]
    y_end = y_interval[1]

    plt.xlim(x_start,x_end)
    plt.ylim(y_start, y_end)

    if keyword == 'tight':
        plt.axis('tight')
    elif keyword == 'equal':
        plt.axis('equal')

    plt.show()

def label_plots(x, title, xlabel, ylabel):
    plt.plot(x, np.sin(x))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Add legend
    plt.plot(x, np.sin(x), '-g', label='sin(x)')
    plt.plot(x, np.cos(x), ':b', label='cos(x)')
    plt.axis('equal')

    plt.legend()

    plt.show()

# Define x
x = np.linspace(0,10,1000)

def main():
    # simple_line_plots(x, num_lines=2)
    # adjusting_line_colors_and_styles(x, adjustment='both')
    # adjusting_axes_limits(x, keyword='equal')
    label_plots(x, "A Sine Curve", "x","sin(x)")

if __name__ == '__main__':
    main()