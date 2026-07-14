import pandas as pd

df = pd.DataFrame({
    "Employee": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Department": ["IT", "IT", "HR", "HR", "IT"],
    "Salary": [70000, 90000, 50000, 65000, 80000]
})

dept_avg = df.groupby("Department")["Salary"].transform("mean")

result = df[df["Salary"] > dept_avg]

print(result)
