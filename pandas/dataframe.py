import pandas as pd
import numpy as np

students = {
    "name": ["hadi", "sahil", "burhan"],
    "age": [15, 17, 20],
    "total_score": [300, 400, 499]
}

m = ["low", "average"]

df = pd.DataFrame(students)


df["class"] = ["8th", "9th", "10th"]

new = pd.DataFrame({
    "name": ["suhail"],
    "age": [19],
    "total_score": [499],
    "class": ["11th"]
})

df = pd.concat([df, new], ignore_index=True)


df["results"] = np.where(
    df["total_score"] <= 400,
    "fail",
    "pass"
)
c = np.random.choice(m, size=len(df))

df["score"] = np.where(
    df["total_score"] == df["total_score"].max(),
    "highest", c)

print(df)