import numpy as np

marks = np.array([40, 50, 60, 70, 80])

minimum = np.min(marks)
maximum = np.max(marks)

n = (marks - minimum) / (maximum - minimum)
print(n.tolist())