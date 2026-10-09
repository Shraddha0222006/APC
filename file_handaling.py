#w---------------------
# file = open("data.txt", "w")

# file.write("Hello Python")
# file.write("\nI am learning file handling.")

# file.close()

# print("Data written successfully")
#append-------------------
# file = open("data.txt", "a")

# file.write("\nThis is append mode.")

# file.close()

# print("Data added successfully")
#r-----------------------------

# file = open("data.txt", "r")

# data = file.read()

# print(data)

# file.close()

#r+  -----------------------------


# file = open("data.txt", "r+")

# print(file.read())

# file.write("\nNew data")

# file.close()

#w+  ----------------------
# file = open("data.txt", "w+")

# file.write("Hello Python")

# file.seek(0)

# print(file.read())

# file.close()

#a+---------------------------
# file = open("data.txt", "a+")

# file.write("\nNew line added")

# file.seek(0)

# print(file.read())

# file.close()
# x-----------------------------
# file = open("newfile.txt", "x")

# file.write("This is a new file")

# file.close()

#tell()-------------------------

# file = open("data.txt", "r")

# print(file.tell())

# data = file.read(5)
# print(data)

# print(file.tell())

# file.close()

#  seck()--------------------------

# file = open("data.txt", "r")

# print(file.read(5))

# file.seek(0)

# print(file.read(5))

# file.close()


