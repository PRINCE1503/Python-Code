# Try Except Exception Handling
a = input("Enter the value of a : ")
b = input("Enter the value of b : ")
try:
    print("The sum of these two numbers is :", int(a)+int(b))
except Exception as Error:
    print("CHECK YOUR INPUT!")
print("Thank you! ")
