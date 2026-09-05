import pandas as pd
df = pd.read_csv("students.csv")
print(df)
print(df.head())
print(df.info())
print(df["math"].mean())
print(df[df["python"]>90])