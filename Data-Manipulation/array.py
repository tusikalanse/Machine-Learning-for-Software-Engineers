import numpy as np
#array with specified type
arr = np.array([2.3, 3.5], dtype=np.float64)
print(arr, arr.dtype)

#cast array into a new type
arr2 = arr.astype(int)
print(arr, arr.dtype)
print(arr2, arr2.dtype)

#NaN inf
arr3 = np.array([np.nan, np.inf, -np.inf])
print(arr3, arr3.dtype)