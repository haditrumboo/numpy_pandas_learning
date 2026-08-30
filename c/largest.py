import numpy as np

a = np.array([10, 45, 23, 67, 12, 89, 34])

sorted_a = np.sort(a)

second_largest = sorted_a[-2]

print(second_largest)