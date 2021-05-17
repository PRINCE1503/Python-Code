# User defined Functions
def average(a, b):
    """Function 'Average' is calculate the Average of two numbers."""
    average = (a+b)/2
    return average


print(average.__doc__)
a = int(input("Enter the First Number : "))
b = int(input("Enter the Second Number : "))
c = average(a, b)
print("The average of these two Number is :", c)
