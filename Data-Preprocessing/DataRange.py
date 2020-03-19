import numpy as np
import sklearn.preprocessing

#x_prop = (x - d_min) / (d_max - d_min)
#x' = x_prop * (r_max - r_min) + r_min

arr = np.array([[1, 100, 2390], [2, 234, 5432], [0, 323, 5555]]) #feature_range=(x, y)

default_scaler = sklearn.preprocessing.MinMaxScaler()
print(default_scaler.fit_transform(arr))
# [[0.5        0.         0.        ]
#  [1.         0.60089686 0.96113744]
#  [0.         1.         1.        ]]

default_scaler = sklearn.preprocessing.MinMaxScaler()
default_scaler.fit(arr)
#print(default_scaler.transform(arr)) the same as line 10
arr2 = np.array([[1, 100, 2390], [2, 100, 1999], [1, 223, 5555]])

print(default_scaler.transform(arr2))
# [[ 0.5         0.          0.        ]
#  [ 1.          0.         -0.1235387 ]
#  [ 0.5         0.55156951  1.        ]]