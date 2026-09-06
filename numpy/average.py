import numpy as np

scores = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80],
    [95, 98, 92]
])

# print(f"average score of each student{np.mean(scores, axis=1).tolist()}")
# print(f"highest score of each sunject {np.max(scores,axis=0).tolist()}")
average = np.mean(scores, axis=1) 
print(f"average score of each students are {average[average > 90].tolist()}")
print(average)