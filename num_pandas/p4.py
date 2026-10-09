
import pandas as pd

# Read CSV file
data = pd.read_csv("students.csv")

# Create a Series from Marks column
s = pd.Series(data["Marks"])

print("Pandas Series:")
print(s)