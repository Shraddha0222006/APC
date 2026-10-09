
import numpy as np

# Create an array of numbers as strings
a = np.array(["1", "2", "3", "4", "5"])

print("Original Array:")
print(a)

# Add character labels to the array
b = np.char.add("Student_", a)

print("\nArray with Character Labels:")
print(b)