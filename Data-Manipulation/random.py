import numpy as np
print(np.random.randint(10))
#np.random.seed
#np.random.shuffle //first dimension only, inplace
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
np.random.shuffle(matrix)
print(repr(matrix))
#maybe array([[1, 2, 3], [7, 8, 9], [4, 5, 6]])

#np.random.uniform : random real numbers
#np.random.normal : Guassian distribution
#np.random.choice : custom sampling