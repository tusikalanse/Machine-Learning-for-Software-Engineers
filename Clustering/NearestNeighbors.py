from sklearn.neighbors import NearestNeighbors
import numpy as np

data1 = np.array([[1, 1], [2, 2.1], [-1, 1], [-1, -0.9]])

nbrs = NearestNeighbors(n_neighbors=3)

nbrs.fit(data1)

data2 = np.array([[2, 2], [1, -1]])

print(nbrs.kneighbors(data2))
# (array([[0.1       , 1.41421356, 3.16227766],
#        [2.        , 2.00249844, 2.82842712]]), array([[1, 0, 2],
#        [0, 3, 2]]))