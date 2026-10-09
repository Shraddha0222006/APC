
# import numpy as np

# # 1D Array
# a = np.array([10, 20, 30, 40, 50])
# print("1D Array:")
# print(a)

# # 2D Array
# b = np.array([[1, 2, 3],
#               [4, 5, 6]])
# print("\n2D Array:")
# print(b)

# # 3D Array
# c = np.array([[[1, 2], [3, 4]],
#               [[5, 6], [7, 8]]])
# print("\n3D Array:")
# print(c)

# ______________________________________________________________________________________________________


import numpy as np


a = np.array([[10, 20],
              [30, 40]])

b = np.array([[2, 4],
              [5, 8]])

print("Array A:")
print(a)

print("\nArray B:")
print(b)

# Addition
print("\nAddition:")
print(np.add(a, b))

# Subtraction
print("\nSubtraction:")
print(np.subtract(a, b))

# Multiplication
print("\nMultiplication:")
print(np.multiply(a, b))

# Division
print("\nDivision:")
print(np.divide(a, b))

# Transpose
print("\nTranspose of Array A:")
print(np.transpose(a))

# Exponential
print("\nExponential of Array A:")
print(np.exp(a))


# _______________________________________________________________________________________________