import numpy as np

#ranged data
print(np.arange(5)) #[0 1 2 3 4]
print(np.arange(3.2)) #[ 0.  1.  2.  3.]
print(np.arange(3.2, 7.2, 0.8)) #[ 3.2  4.   4.8  5.6  6.4]

#linspace
print(np.linspace(2.0, 3.0, num=5))
#array([2.  , 2.25, 2.5 , 2.75, 3.  ])
print(np.linspace(2.0, 3.0, num=5, endpoint=False))
#array([2. ,  2.2,  2.4,  2.6,  2.8])
print(np.linspace(2.0, 3.0, num=5, retstep=True))
#(array([2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
print(np.linspace(5, 11, num=5))
#[  5.    6.5   8.    9.5  11. ]
print(np.linspace(5, 11, num=5, dtype=np.int32))
#[ 5  6  8  9 11]

#reshape
arr = np.arange(8)
reshaped_arr = arr.reshape(4, 2)
print(repr(reshaped_arr))
#array([[0, 1], [2, 3], [4, 5], [6, 7])
#one dimision can be -1, the value is inferred from the length of th array and remaining dimisions
reshaped_arr = arr.reshape(2, -1, 2)
print(repr(reshaped_arr))
#array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
#Error : arr.reshape(4, 3)

#flatten : reshape an array into a 1D array
arr2 = reshaped_arr.flatten()
print(repr(arr2))
#array([0, 1, 2, 3, 4, 5, 6, 7])

#transpose axes(permutaion of range(n))
arr = np.arange(24)
arr = np.reshape(arr, (3, 4, 2))
transposed = np.transpose(arr, axes=(1, 2, 0))
print(arr.shape)
#(3, 4, 2)
print(transposed.shape)
#(4, 2, 3)

#np.zeros, np.ones    fill array with 0/1
#np.zeros_like, np.ones_like
arr = np.array([[1, 2], [3, 4]])
print(repr(np.zeros_like(arr)))
#array([[0, 0], [0, 0]])
