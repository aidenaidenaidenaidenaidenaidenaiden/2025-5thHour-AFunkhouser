import random
from base64 import a85decode

cur = random.randint(2, 13)
nex = random.randint(2, 13)
'''
while True:
    c = input(f"{cur} is your number. Will the next be higher or lower?   ")
    if nex == cur:
        nex = random.randint(1, 12)
    if c == "higher" and cur < nex:
        print(f"Correct! {nex} was higher than {cur}.")
        cur = random.randint(1, 12)
        cur, nex = nex, cur
    elif c == "lower" and cur > nex:
        print(f"Correct! {nex} was lower than {cur}.")
        cur = random.randint(1, 12)
        cur, nex = nex, cur
    elif c == "lower" and cur < nex:
        print(f"Wrong. {nex} was higher than {cur}.")
        d = input("Do you want to continue? yes/no  ")
        if d == "yes":
            continue
        else:
            break
    elif c == "higher" and cur > nex:
        print(f"Wrong. {nex} was lower than {cur}.")
        d = input("Do you want to continue? yes/no  ")
        if d == "yes":
            continue
        else:
            break
    else:
        print("CHOOSE ONLY WHAT I TOLD YOU TO CHOOSE")
        d = input("Do you want to continue? yes/no  ")
        if d == "yes":
            continue
        else:
            break
            '''
ezlist = ["rock", "paper", "scissors"]
random.shuffle(ezlist)

print("rock paper scissors")

bleh = input("do you want to play against easy or hard npc? ")
if bleh == "easy":
    while True:
        ans = input("choose rock, paper, or scissors  ")
        random.shuffle(ezlist)
        if ans == "rock" :
            print(ezlist[0])
            if ezlist[0] == "rock":
                continue
            if ezlist[0] == "paper":
                print("YOU LOSE!!!")
                break
            if ezlist[0] == "scissors":
                print("YOU WIN!!!")
                break
        if ans == "paper" :
            print(ezlist[0])
            if ezlist[0] == "rock":
                print("YOU WIN!!!")
                break
            if ezlist[0] == "paper":
                continue
            if ezlist[0] == "scissors":
                print("YOU LOSE!!!")
                break
        if ans == "scissors" :
            print(ezlist[0])
            if ezlist[0] == "rock":
                print("YOU LOSE!!!")
                break
            if ezlist[0] == "paper":
                print("YOU WIN!!!")
            if ezlist[0] == "scissors":
                continue
if bleh == "hard":
    ans = input("choose rock, paper, or scissors  ")
    if ans == "rock" :
        print("paper")
        print("YOU LOSE!!!")
    if ans == "paper" :
        print("scissors")
        print("YOU LOSE!!!")
    if ans == "scissors":
        print("rock")
        print("YOU LOSE!!!")