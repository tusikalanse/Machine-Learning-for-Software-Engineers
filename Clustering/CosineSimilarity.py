from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


data1 = np.array([[1, 1], [2, 2.1], [-1, 1], [-1, -0.9]])

print(cosine_similarity(data1))
# [[ 1.00000000e+00  9.99702691e-01  2.23711432e-17 -9.98617829e-01]
#  [ 9.99702691e-01  1.00000000e+00  2.43829925e-02 -9.97039389e-01]
#  [ 2.23711432e-17  2.43829925e-02  1.00000000e+00  5.25588331e-02]
#  [-9.98617829e-01 -9.97039389e-01  5.25588331e-02  1.00000000e+00]]

data2 = np.array([[2, 2], [1, -1]])
print(cosine_similarity(data1, data2))
# [[ 1.00000000e+00 -2.23711432e-17]
#  [ 9.99702691e-01 -2.43829925e-02]
#  [ 2.23711432e-17 -1.00000000e+00]
#  [-9.98617829e-01 -5.25588331e-02]]