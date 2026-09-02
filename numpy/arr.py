import numpy as np

a = np.array([15, 22, 8, 31, 14, 5, 40, 19])

f = a[(a > 10) & (a < 30)]

print(f)
