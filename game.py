import random
print("g : gun\ns : snake\nw : water")
computer = random.choice([-1, 0, 1])
youn = input("Enter your Choice among (s,w,g): ")
youDict = {"s": 1, "w": -1, "g": 0}

reDict = {1 : "snake", -1 : "water", 0 : "gun"}
you = youDict[youn]

print(f"You choose {reDict[you]}\ncomputer choose {reDict[computer]}")

if (computer == you):
    print("Draw B/w You & Computer")
elif (computer == -1 and you == 1):
    print("you win!")
elif (computer == -1 and you ==  0):
    print("computer win!")
elif (computer == 1 and you ==  -1):
    print("computer win!")
elif (computer == 0 and you ==  1):
    print("computer win!")
elif (computer == 1 and you == 0):
    print("you win!")
elif (computer == 0 and you == -1):
    print("you win!")
else:
    print("You may enter something wrong")

