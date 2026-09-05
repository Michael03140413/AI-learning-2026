import pandas as pd

data = {
    "name": ["Tom", "Jack", "Alice", "Mike", "Lucy"],
    "math": [89, 77, 91, 93, 91],
    "python": [83, 84, 95, 82, 93]
}

df = pd.DataFrame(data)

print(df)
print("\nMath average:", df["math"].mean())
print("Python average:", df["python"].mean())

high_score = df[df["python"] > 90]
print("\nStudents with Python score above 90:")
print(high_score)
df["average"] = (df["math"]+df["python"])/2
print(df)
print("\nStudents with math high scores:",df[df["math"]>90])
print("\nStudents with average score above 90:",df[df["average"]>90])