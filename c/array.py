import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])

print(np.intersect1d(a, b))
print(np.setdiff1d(a, b))
print(np.setxor1d(a, b))

