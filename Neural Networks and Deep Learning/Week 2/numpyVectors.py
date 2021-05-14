import numpy as np

a = np.random.randn(5)
print(a)
print(a.shape)  # this will be a (5,), which is called a rank 1 array
print(a.T)  # same as A
print(np.dot(a, a.T))   # it prints a number, not a matrix

a = np.random.randn(5, 1)   # it is preferable to init the array with both rows and columns
print(a)    # column vector
print(a.T)  # row vector
print(np.dot(a, a.T))   # this prints a matrix of size 5x5

assert(a.shape == (5, 1))   # you can use asserts to always check if you have the right shape
a = a.reshape((5, 1))   # and you can also reshape to get the right shape