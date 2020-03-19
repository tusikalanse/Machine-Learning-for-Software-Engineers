#Learn how to apply L2 normalization to data
import numpy as np
import sklearn.preprocessing

#x' = x / sqrt(sigma_{i=1}^n((x_i)^2))

arr = np.array([[4, 1, 2, 2],
       [3, 4, 0, 0],
       [7, 5, 9, 2]])

#apply L2 normalization to each row
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!each row!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

normalizer = sklearn.preprocessing.Normalizer()

print(normalizer.fit_transform(arr))
# [[0.8        0.2        0.4        0.4       ]
#  [0.6        0.8        0.         0.        ]
#  [0.55513611 0.39652579 0.71374643 0.15861032]]