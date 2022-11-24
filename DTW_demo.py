__updated__ = '2022-11-24 17:43:42'
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)



import numpy as np

# We define two sequences x, y as numpy array
# where y is actually a sub-sequence from x
x = np.array([2, 0, 1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)
y = np.array([1, 1, 2, 4, 2, 1, 2, 0]).reshape(-1, 1)

manhattan_distance = lambda x, y: np.abs(x - y)

from DTW_demo import dtw
d, cost_matrix, acc_cost_matrix, path = dtw(x, y, dist=manhattan_distance)

print(d)

# You can also visualise the accumulated cost and the shortest path

# import matplotlib.pyplot as plt
# plt.imshow(acc_cost_matrix.T, origin='lower', cmap='gray', interpolation='nearest')
# plt.plot(path[0], path[1], 'w')
# plt.show()

import time as t
time1 = t.time()
np.random.seed(0)
a = np.random.normal(3, 2.5, size=(2, 1000))
from DTW_demo import DTW_demo
from numpy.linalg import norm
dist_dtw, cost, acc_cost, path = dtw(
    a[0].reshape(-1, 1),
    a[1].reshape(-1, 1),
    dist=lambda x, y: norm(x - y, ord=1)
)
time2 = t.time()