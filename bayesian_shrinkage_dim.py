import numpy as np
import matplotlib.pyplot as plt

n = np.arange(33, 3202, 1)
rating = (-1, 0, 1)

m = 335
sigma = -0.101

def score(n, s, m, sigma):
    """ Calcola il punteggio bayesiano con shrinkage. """
    return (n * s + m * sigma) / (n + m)

min = score(min(n), -1, m, sigma)
max = score(max(n), 1, m, sigma)

score_min_max = (score(n, 1, m, sigma) - min) / (max - min)

plt.scatter(n, score_min_max)
plt.show()