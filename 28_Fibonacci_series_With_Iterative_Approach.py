# Fibonacci series With Iterative Approach
# Iterative Approach
def fib_iterative(n):
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a+b
    return a


try:
    A = int(input("Enter the Index number you want to know wich number is at this position in fibonacci serise : "))
    print("The value of fibonacci series at index Number",
          A, "is : ", fib_iterative(A))
except Exception as a:
    print("ENTER VALID INPUT!")
