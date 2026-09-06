import numpy as np
rr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# print(rr + 10)
# print(rr * [1, 10, 100])

print(rr[rr % 2 == 0])