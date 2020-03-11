import numpy as np

arr = np.array([[0, 2, 3],
                [1, 3, -6],
                [-3, -2, 1]])
print(repr(arr == 3))
#array([[False, False,  True], [False,  True, False], [False, False, False]], dtype=bool)
#np.isnan

#np.where with 1 argument
arr = np.array([[0, 2, 3],
                [1, 0, 0],
                [-3, 0, 0]])
x_ind, y_ind = np.where(arr != 0)
print(repr(np.where(arr != 0)))
print(repr(x_ind)) # x indices of non-zero elements
print(repr(y_ind)) # y indices of non-zero elements
print(repr(arr[x_ind, y_ind]))
# (array([0, 0, 1, 2]), array([1, 2, 0, 0]))
# array([0, 0, 1, 2])
# array([1, 2, 0, 0])
# array([ 2,  3,  1, -3])


#np.where with 3 arguments
np_filter = np.array([[True, False], [False, True]])
positives = np.array([[1, 2], [3, 4]])
print(repr(np.where(np_filter, positives, -1)))
#array([[ 1, -1], [-1,  4]])

#np.any, np.all axis=