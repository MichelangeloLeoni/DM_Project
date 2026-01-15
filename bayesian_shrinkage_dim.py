import numpy as np
import matplotlib.pyplot as plt

n = np.arange(33, 3202, 1)
rating = (-1, 0, 1)

m = 335
sigma = -0.101

def score(n, s, m, sigma):
    """ Calcola il punteggio bayesiano con shrinkage. """
    return (n * s + m * sigma) / (n + m)

min = score(max(n), -1, m, sigma)
max = score(max(n), 1, m, sigma)

score_min_max1 = (score(n, 1, m, sigma) - min) / (max - min)
score_min_max0 = (score(n, 0, m, sigma) - min) / (max - min)
score_min_maxm1 = (score(n, -1, m, sigma) - min) / (max - min)

# Subplot of three different ratings
plt.figure(figsize=(10, 6))
plt.plot(n, score_min_max1, label='Rating = 1', color='blue')
plt.plot(n, score_min_max0, label='Rating = 0', color='green')
plt.plot(n, score_min_maxm1, label='Rating = -1', color='red')

# dashed areas under the curves with legend labels
blue_patch = plt.fill_between(n, np.min(score_min_max1), np.max(score_min_max1), color='blue', alpha=0.05, hatch='///', label='Sector 1: Rating = 1')
green_patch = plt.fill_between(n, np.min(score_min_max0), np.max(score_min_max0), color='green', alpha=0.05, hatch='///', label='Sector 2: Rating = 0')
red_patch = plt.fill_between(n, np.min(score_min_maxm1), np.max(score_min_maxm1), color='red', alpha=0.05, hatch='///', label='Sector 3: Rating = -1')


plt.title('Normalized Bayesian Shrinkage Score vs Number of Ratings')
plt.xlabel('NumUserRatings (n)')
plt.ylabel('Min-Max Normalized WeightedRating')
# insert mean and sigma values in the legend with enhanced styling
plt.text(75, 1.05, f'Mean (m): {m}\nSigma (σ): {sigma}', fontsize=8, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.8', facecolor='white', edgecolor='black', linewidth=2, alpha=0.9),
         verticalalignment='top')

# Add three separate legends positioned at the right, slightly above their respective curves
ax = plt.gca()
y_offset = 0.05  # Offset above the curves

# Get the final y-values for each curve
y_val_blue = score_min_max1[-1]
y_val_green = score_min_max0[-1]
y_val_red = score_min_maxm1[-1]

# Position legends at the right, slightly above each curve
ax.text(n[-1] - 375, y_val_blue + y_offset, 'Rating = 1', fontsize=9, color='blue', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='blue', alpha=0.8))
ax.text(n[-1] - 375, y_val_green + y_offset, 'Rating = 0', fontsize=9, color='green', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='green', alpha=0.8))
ax.text(n[-1] - 375, y_val_red + y_offset, 'Rating = -1', fontsize=9, color='red', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='red', alpha=0.8))
plt.xlim(0, 3200)
plt.ylim(-0.1, 1.1)

plt.grid()
plt.savefig('bayesian_shrinkage_dim.png', dpi=900)
plt.show()