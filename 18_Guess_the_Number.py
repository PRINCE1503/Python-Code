# Guess the Number
n = 49
Total_Guess = 1
print("This is a Number guessing Game")
print("You have 9 chances to guess right Number")
while(Total_Guess <= 9):
    i = int(input("Guess the Number: "))
    if i <= 10:
        print("You entered a very small Number, Enter larger Number\n")
    elif i <= 30:
        print("Yoy entered a too small Number, Enter larger Number\n")
    elif i <= 40:
        print("You entered a smaller Number, Enter larger Number\n")
    elif i < 48:
        print("You entered a smaller Number, Enter larger Number\n")
    elif i == 49:
        print("CONGRATULATIONS! YOU WIN!")
        print("You have take", Total_Guess,
              "chances to guess correct Number\n")
        break
    elif i <= 70:
        print("You entered a larger Number, Enter smaller Number\n")
    elif i <= 90:
        print("You entered a too larger Number, Enter smaller Number\n")
    elif i <= 100:
        print("You entered a very larger Number, Enter smaller number\n")
    elif i > 100:
        print("Please Enter smaller Number")
    print("You have", 9-Total_Guess, "guesses left")
    Total_Guess = Total_Guess+1
if Total_Guess > 9:
    print("!! GAME OVER !!")
    print("49 is a Correct Number")
