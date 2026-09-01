import pandas as pd
import numpy as np

students = {
    "name": ["hadi", "sahil", "burhan"],
    "age": [15, 17, 20],
    "total_score": [300, 400, 499]
}
m = ["low", "average"]

df = pd.DataFrame(students)
c = np.random.choice(m, size=len(df))
df["class"] = ["8th", "9th", "10th"]

# Add grade
df["results"] = np.where(df["total_score"] <= 400, "fail", "pass")

df["score"] = np.where(df["total_score"] == df["total_score"].max(), "highest" ,c)
print(df)