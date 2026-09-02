import pandas as pd
import numpy as np

students = {
    "name": ["Hadi", "Sahil", "Burhan", "Suhail", "Ayan"],
    "age": [15, 17, 20, 19, 16],
    "math": [85, 72, 95, 60, 88],
    "english": [78, 80, 90, 65, 92]
}



df = pd.DataFrame(students)

df["total"] = df["math"] + df["english"]
df["score"] = np.where(df["total"] > 150, "pass", "fail")
df["grade"] = np.where(df["total"] == df["total"].max(), "highest", " ")

print(df)
