import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Defining the function
def f(x):
    return 0.25 * (x + 4) * (x + 1) * (x - 2)

# Generate x values
x = np.linspace(-4, 4, 500)

# Calculate y values
y = f(x)

# Find the minimum of the function
min_index = np.argmin(y)
x_min = x[min_index]
y_min = y[min_index]

# Set the size of the figure
dpi = 72
fig, ax = plt.subplots(figsize=(1280/dpi, 720/dpi), dpi=dpi)

# Plot the function
ax.plot(x, y, label='f(x)')

# Annotate the minimum
ax.annotate('Minimum', xy=(x_min, y_min), xytext=(x_min, y_min+5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='center')

# Create an mbedded figure to emphasize the minimum
ax_inset = fig.add_axes([0.5, 0.5, 0.2, 0.2]) # Inset axes: [left, bottom, width, height]
ax_inset.plot(x, y)
ax_inset.set_xlim(x_min - 1, x_min + 1)
ax_inset.set_ylim(y_min - 1, y_min + 1)
ax_inset.axhline(y=y_min, color='grey', linestyle='--')
ax_inset.axvline(x=x_min, color='grey', linestyle='--')

# Highlight the minimum on the inset
ax_inset.plot(x_min, y_min, 'ro')

# Set plot labels
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Initialize a red dot on the plot at the minimum
red_dot, = ax.plot([], [], 'ro', ms=5)

#saving the figure
plt.savefig('curve_with_segment.png')


# animation from min to max
def animate(i):
    red_dot.set_data([x[i]], [y[i]])
    return red_dot,

# Create the animation object
ani = FuncAnimation(fig, animate, frames=len(x), interval=10, blit=True)

#Save the animation to an mp4 file
mp4_filename = 'animated_curve.mp4'
ani.save(mp4_filename, writer='ffmpeg', fps=30)

plt.show()
