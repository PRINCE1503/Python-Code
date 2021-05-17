# # Rock Paper Scissor Game
import random
print("\n\t\t\t\tWELCOME TO GAME OF ROCK - PAPER - SCISSOR\n")
list = ["R", "P", "S"]
a = int(input("How many times you want to play this game : "))
yp = 0
cp = 0
tc = 0

print()

while tc < a:
    print("ROUND", tc+1)
    i = input("Choose Rock for 'R', Paper for 'P', Scissor for 'S' : ")
    c = random.choice(list)
    if i == c:
        print(f"You and computer both choose '{i}'")
        yp += 1
        cp += 1
        print("It's a Tie!")
        print(f"Your Score : {yp}\nComputer Score : {cp}")
    elif i == "R" and c == "P":
        print(f"You choose {i} & Computer choose {c}")
        cp += 1
        print("Computer got it!")
        print(f"Your Score : {yp}\nComputer Score : {cp}")
    elif i == "R" and c == "S":
        print(f"You choose {i} & Computer choose {c}")
        yp += 1
        print("You got it!")
        print(f"Your Score : {yp}\nComputer Score : {cp}")
    elif i == "P" and c == "S":
        print(f"You choose {i} & Computer choose {c}")
        cp += 1
        print("Computer got it!")
        print(f"Your Score : {yp}\nComputer Score : {cp}")
    elif i == "P" and c == "R":
        print(f"You choose {i} & Computer choose {c}")
        yp += 1
        print("You got it!")
        print(f"Your Score : {yp}\nComputer Score : {cp}")
    elif i == "S" and c == "R":
        print(f"You choose {i} & Computer choose {c}")
        cp += 1
        print("Computer got it!")
        print(f"Your Score : {yp}\nComputer Score : {cp}")
    elif i == "S" and c == "P":
        print(f"You choose {i} & Computer choose {c}")
        yp += 1
        print("You got it!")
    else:
        print("WRONG INPUT!")
    tc = tc+1
    print(f"You have {a-tc} chances left.\n")
    print("-----------------------------------------------------\n")
print("!! -- GAME OVER -- !!\n\n")
if yp == cp:
    print("It's a Tie!")
elif yp < cp:
    print("Bad Luck! You Lose!")
else:
    print("Congratulations! You win!")
