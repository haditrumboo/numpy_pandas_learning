import numpy as np

a = np.array([12, 5, 18, 3, 20, 7, 9, 25])
# a[a < 10] = 0
# print(a)

f = np.where(a < 10 , 0, a)
print(f)