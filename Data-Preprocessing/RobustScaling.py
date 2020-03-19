#Learn how to scale data without being affected by outliers
import numpy as np
import sklearn.preprocessing

#x' = (x - x.median) / IQR
arr = np.array([[1, 100], 
             [2, 80],
             [3, 75],
             [4, 1930],
             [5, 120]])

robust_scaler = sklearn.preprocessing.RobustScaler()
print(robust_scaler.fit_transform(arr))
# [[-1.     0.   ]
#  [-0.5   -0.5  ]
#  [ 0.    -0.625]
#  [ 0.5   45.75 ]
#  [ 1.     0.5  ]]