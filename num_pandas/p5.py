
import pandas as pd

# Read CSV file
data = pd.read_csv("students.csv")

# Create DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Student DataFrame:")
print(df)