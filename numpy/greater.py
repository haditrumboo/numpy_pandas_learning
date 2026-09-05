import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# print(arr[arr > 50])
print(arr[0:1].max())
print(arr[1:2].max())
print(arr[2].max())
print(np.max(arr, axis=1))