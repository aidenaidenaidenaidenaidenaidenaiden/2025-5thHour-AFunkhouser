import random
import time
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
    #New game here
a = random.randint(1, 1000)
b = random.randint(1, 1000)
times = 0
while a > b or b > a:
    times += 1
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
if a == b:
    print(times)
'''
def q():
    a = input("Is sam an idiot? yes/yes  ")
    if a == "yes":
        print("Correct!")
    elif a == "nes":
        print("Ness? PK FIRE! Now try again.")
        q()
    elif a == "no":
        print("WRONG TRY AGAIN")
        q()
    elif a == "yo":
        print("yo-yo? Ness' yo-yo? Try again.")
        q()
    else:
        print("Try again.")
        q()
def c():
    b = input("Is sir Aiden the handsome, majestic, and great an idiot? no/no  ")
    if b == "no":
        print("Correct!")
    elif b == "nes":
        print("Ness? PK FIRE! Now try again.")
        c()
    elif b == "yes":
        print("NO HE ISNT TRY AGAIN")
        c()
    elif b == "yo":
        print("yo-yo? Ness' yo-yo? Try again.")
        c()
    else:
        print("Try again.")
        c()
q()
c()