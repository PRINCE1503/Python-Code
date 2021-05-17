# Factorial with Iterative & recursive approach
# Iterative approach
def factorial_Iterative(n):
    a = 1
    for i in range(n):
        a = a*(i+1)
    return a


try:
    n = int(input("Ente the number you want factorial : "))
    print("The factorial of Number", n,
          "with Iterative approach is :", factorial_Iterative(n))
except Exception as E:
    print("ENTER VALID INPUT!!")


# Recursive approach
def factorial_Recursive(n):
    if n == 1 or 0:
        return 1
    else:
        return n*(factorial_Recursive(n-1))


print("The factorial of Number", n,
      "with Recursive approach is :", factorial_Recursive(n))
