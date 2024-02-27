import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean = [1, 1]
cov = [[1, 0.2], [0.2, 0.8]]  # covariance matrix
sample_size = 10000  # large sample size

#large sample from a bivariate normal distribution
sample = np.random.multivariate_normal(mean, cov, sample_size)

# Create a figure
fig = plt.figure(figsize=(10, 10))
gs = fig.add_gridspec(2, 2, width_ratios=(2, 7), height_ratios=(7, 2),
                      left=0.1, right=0.9, bottom=0.1, top=0.9, 
                      wspace=0.1, hspace=0.1)

# Scatter plot
ax_scatter = fig.add_subplot(gs[0, 1])
ax_scatter.scatter(sample[:, 0], sample[:, 1], alpha=0.5)

# Histogram for X1 (inverted)
ax_histx = fig.add_subplot(gs[0, 0], sharey=ax_scatter)
ax_histx.hist(sample[:, 1], bins=50, orientation='horizontal', density=True, alpha=0.7)
ax_histx.invert_xaxis()  # Invert X axis to have the histogram on the left
ymin, ymax = ax_histx.get_xlim()
x2 = np.linspace(ymin, ymax, 100)
ax_histx.plot(norm.pdf(x2, mean[1], np.sqrt(cov[1][1])), x2, 'k', linewidth=2)

# Histogram for X2 (on top)
ax_histy = fig.add_subplot(gs[1, 1], sharex=ax_scatter)
ax_histy.hist(sample[:, 0], bins=50, density=True, alpha=0.7)
ax_histy.invert_yaxis()  # Invert Y axis to have the histogram on top
xmin, xmax = ax_histy.get_ylim()
x1 = np.linspace(xmin, xmax, 100)
ax_histy.plot(x1, norm.pdf(x1, mean[0], np.sqrt(cov[0][0])), 'k', linewidth=2)

# move axis
ax_histx.yaxis.tick_right()
ax_histx.yaxis.set_label_position("right")

# formatting the plots
ax_scatter.tick_params(axis="both", which="both", bottom=False, top=False, labelbottom=False, left=False, right=False, labelleft=False)
ax_histx.tick_params(axis="y", direction="in", pad= -25)
ax_histy.tick_params(axis="x", direction="in", pad= -25)

# Set labels and title
ax_scatter.set_xlabel('$X_1$', fontsize=12)
ax_scatter.set_ylabel('$X_2$', fontsize=12)
ax_histx.set_xlabel('Density', fontsize=12)
ax_histy.set_ylabel('Density', fontsize=12)
fig.suptitle('Bivariate Normal Distribution with Marginals', fontsize=16)

# Hide x labels and tick labels for left plots and y ticks for bottom plots.
plt.setp(ax_histx.get_xticklabels(), visible=False)
plt.setp(ax_histy.get_yticklabels(), visible=False)

# Hide hist plots' spines
ax_histx.spines['top'].set_visible(False)
ax_histx.spines['right'].set_visible(True)
ax_histx.spines['left'].set_visible(False)
ax_histx.spines['bottom'].set_visible(False)
ax_histy.spines['top'].set_visible(False)
ax_histy.spines['right'].set_visible(False)
ax_histy.spines['left'].set_visible(False)
ax_histy.spines['bottom'].set_visible(True)

# Add a legend with a dummy handle
handles = [plt.Line2D([0], [0], color='black', lw=2)]
labels = ['Analytical PDF']
fig.legend(handles, labels, loc='upper right', fontsize=14)
plt.savefig('bivariate_normal_distribution.png')
# Show the plots
plt.show()

