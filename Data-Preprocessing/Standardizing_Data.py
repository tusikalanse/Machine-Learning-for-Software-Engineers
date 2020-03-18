import sklearn.preprocessing
import numpy as np

#standard data : mean = 0, standard deviation = 1

arr = np.array([[1, 100, 2390], [2, 234, 5432], [0, 323, 5555]])

std = sklearn.preprocessing.scale(arr)

print(std)
# [[ 0.         -1.29834493 -1.41338128]
#  [ 1.22474487  0.16365692  0.66467858]
#  [-1.22474487  1.134688    0.7487027 ]]

print(std.mean(axis=0))
# [0.00000000e+00 0.00000000e+00 3.70074342e-17]

print(std.std(axis=0))
# [1. 1. 1.]