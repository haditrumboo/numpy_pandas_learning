import pandas as pd



df = pd.read_csv("files/sales.csv")
# print(file.to_string())
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df[["product", "city", "price"]])
# print(df["price"].max())
# print(df[df["city"] == "Delhi"])
# print(df[
#     (df["quantity"] > 5) &
#     (df["city"] == "Mumbai")
# ])
# print(df[df["product"].isin(["Laptop", "Keyboard"])])
# print(df.sort_values("price", ascending=False))
# print(df.groupby("city")["quantity"].sum())
# print(df.groupby("product")["price"].mean())
# print(df[df.isnull().any(axis=1)])
df["salesperson"] = df["salesperson"].fillna("adil")
df["salesperson"] =df["salesperson"].str.upper()
print(df)

