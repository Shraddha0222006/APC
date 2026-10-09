# paragraph = """
# My name is Shraddha.
# I am learning Python.
# Python is easy to understand.
# """

# print(paragraph)

#######################################

#st1
# string = input("Enter a string: ")

# count = 0

# for i in string:
#     count = count + 1

# print("Length of string =", count)

##########################
# string = input("Enter a string: ")

# vowels = 0
# consonants = 0
# digits = 0
# spaces = 0
# special = 0

# for ch in string:
#     if ch in "aeiouAEIOU":
#         vowels = vowels + 1
#     elif ch.isalpha():
#         consonants = consonants + 1
#     elif ch.isdigit():
#         digits = digits + 1
#     elif ch == " ":
#         spaces = spaces + 1
#     else:
#         special = special + 1

# print("Vowels =", vowels)
# print("Consonants =", consonants)
# print("Digits =", digits)
# print("Spaces =", spaces)
# print("Special Characters =", special)
####################################################
# string=input("enter the string")
# upper=0
# lower=0
# for ch in string:
#     if ch.isupper():
#         upper=upper+1
#     elif ch.islower():
#         lower=lower+1
# print("uppe=", upper)
# print("lowe=", lower)

##############################

# string = input("Enter a string: ")

# print("First character =", string[0])
# print("Last character =", string[-1])

###############################
# string = input("Enter a string: ")

# reverse = ""

# for ch in string:
#     reverse = ch + reverse

# print("Reversed String =", reverse)
#########################################
# string = input("Enter a string: ")

# reverse = ""

# for ch in string:
#     reverse = ch + reverse

# if string == reverse:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

################################
# string = input("Enter a string: ")

# old = input("Enter character to replace: ")
# new = input("Enter new character: ")

# result = ""

# for ch in string:
#     if ch == old:
#         result = result + new
#     else:
#         result = result + ch

# print("New String =", result)
#####################################

# string = input("Enter a string: ")

# result = ""

# for ch in string:
#     if ch != " ":
#         result = result + ch

# print("String without spaces =", result)
########################################################

# string = input("Enter a sentence: ")

# count = 0

# if string != "":
#     count = 1

# for ch in string:
#     if ch == " ":
#         count = count + 1

# print("Total words =", count)