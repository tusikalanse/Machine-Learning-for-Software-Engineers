import numpy as np

#np.sum, np.cumsum -> prefixsum
arr = np.array([1, 2, 3])
print(np.cumsum(arr))
#[1 3 6]

#np.concatenate((arr1, arr2...), axis=0)
arr2 = np.array([4, 5, 6])
print(np.concatenate([arr, arr2]))
#[1 2 3 4 5 6]