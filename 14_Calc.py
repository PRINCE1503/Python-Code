# Calc
print("Enter...\n", "'+' for Addition\n",
      "'-' for subtraction\n", "'*' for mutiplication")
print(" '/' for Devision\n", "'**' for power\n")
print("Enter the Opertion : ", end="")
Operation = input()
a = int(input("Enter the first Number : "))
b = int(input("Enter the second Number : "))
if Operation == '+':
    print(a, "+", b, "=", a+b)
elif Operation == '-':
    print(a, "-", b, "=", a-b)
elif Operation == '*':
    print(a, "*", b, "=", a*b)
elif Operation == '/':
    print(a, "/", b, "=", a/b)
elif Operation == '**':
    print(a, "^", b, "=", a**b)
else:
    print("Error! Check your input")
