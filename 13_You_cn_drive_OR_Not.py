# You can drive or not
age = int(input("Enter your age : "))
if age > 100:
    print("Error! PLease Check your age!")
elif age == 18:
    print("We will think about you.")
elif age > 18:
    print("You can drive!")
else:
    print("You can't drive!")
