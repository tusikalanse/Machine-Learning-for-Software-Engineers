import numpy as np

arr = np.array([1, 2, 3, 4])
print(repr(arr + 1))
#array([2, 3, 4, 5]), +, -, *, /， //， %， **

def f(t):
    return 2 * t + 1
print(repr(f(arr)))
#array([3, 5, 7, 9]), np.exp, np.exp2, np.log, np.log10
#np.power(base, power) base / power can be an array
#matrix multiciplication : np.matmul(arr1, arr2)
#np.dot(arr1, arr2), arr1.dot(arr2)