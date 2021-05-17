# Interchange Value
a = input("Enter the value of a : ")
b = input("Enter the value of b : ")
print("The value of a is :", a, end="\n")
print("The value of b is :", b)
a, b = b, a
print("Now, The value of a is :", a, end="\n")
print("The value of b is :", b)
