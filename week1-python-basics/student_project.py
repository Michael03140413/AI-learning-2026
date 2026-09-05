import pandas as pd
df = pd.read_csv("students.csv")
print(df.head())
df.info()
df["average"] = (df["math"] + df["python"])/2
print(df[df["average"]>90])
def classify_score(score):
    if score >90:
        return"Execellent"
    elif score>80:
        return"Good"
    else:
        return"need improvement"
df["level"] = df["average"].apply(classify_score)
print(df)
best_student = df.loc[df["average"].idxmax()]
print(best_student)
print("Class Average:",df["average"].mean())
df.to_csv("students_results.csv",index=False)
import matplotlib.pyplot as plt
plt.bar(df["name"],df["average"])
plt.xlabel("Students' Names")
plt.ylabel("Students' Average Scores")
plt.title("Students' Study")
plt.show()