import numpy as np

#multi_dimension slice 
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[0:1, 1:])
#[[2 3]]
print(arr[:, -1])
#[3 6 9]

#argmin, argmax, return the index of the minimum/maximum element
print(np.argmin(arr[2]))
#0
print(np.argmax(arr))
#8 flattened
#axis : specify the dimision
arr = np.array([[-2, -1, -3, 4],
                [4, 5, -6, 7],
                [-3, 9, 1, 123]])
print(repr(np.argmin(arr, axis=0)))
print(repr(np.argmin(arr, axis=1)))
print(repr(np.argmax(arr, axis=-1)))
#array([2, 0, 1, 0])
#array([2, 2, 0])
#array([3, 3, 3])