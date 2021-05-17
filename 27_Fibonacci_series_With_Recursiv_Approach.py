# Fibonacci series With Recursiv Approach
def fib_recursive(n):
    n+1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recursive(n-1)+fib_recursive(n-2)


try:
    a = int(input("Enter the Index number you want to know wich number is at this position in fibonacci serise : "))
    print("The value of fibonacci series at index Number",
          a, "is : ", fib_recursive(a))
except Exception as a:
    print("ENTER VALID INPUT!")
