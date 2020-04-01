#将数据分群
#首先随意指定若干中心，然后按距离分类，每一类的中心作为新的中心继续此操作
#迭代若干次直到收敛

import numpy as np
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
# predefined data

data = np.array([
    [1, 2, 3, 4],
    [-1, -2, -3, -4],
    [-3, 2, 4, 2],
    [12, 324, 9, 4],
    [12, 12, -32, 43],
    [23, 12, 46, -33]
])

kmeans.fit(data)
# cluster assignments
print('{}\n'.format(repr(kmeans.labels_)))
# array([0, 0, 0, 1, 0, 2], dtype=int32)
# centroids
print('{}\n'.format(repr(kmeans.cluster_centers_)))

# array([[  2.25,   3.5 ,  -7.  ,  11.25],
#        [ 12.  , 324.  ,   9.  ,   4.  ],
#        [ 23.  ,  12.  ,  46.  , -33.  ]])

new_obs = np.array([
  [5.1, 3.2, 1.7, 1.9],
  [6.9, 3.2, 5.3, 2.2]])
# predict clusters
print('{}\n'.format(repr(kmeans.predict(new_obs))))
# array([0, 0], dtype=int32)