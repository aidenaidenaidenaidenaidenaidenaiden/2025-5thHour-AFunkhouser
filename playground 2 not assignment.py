import random
import time
def pi():
    print("Would you like to see a clock? Yes / No")
    a = input()
    if a == "Yes" or a == "yes":
        h = 0
        m = 0
        s = 0
        ms = 0
        while ms > -1:
            time.sleep(0.01)
            print(f"{h}:{m}:{s}:{ms}")
            ms = ms + 1
            if ms == 100:
                ms = 0
                s = s + 1
            if s == 60:
                s = 0
                m = m + 1
            if m == 60:
                m = 0
                h = h + 1
    elif a == "No" or a == "no":
        print("Here's a gambling game. When given a number 1-15, guess if the next is higher or lower.")
        print("If the outcome is equal, it won't be counted against you.")
        while 0 < 1:
            ran1 = random.randint(1, 15)
            ran2 = random.randint(1, 15)
            print(f"{ran1} is your number. Will your next be higher or lower?")
            ans = input()
            if ans == "Higher" or ans == "higher" and ran1 <= ran2:
                print(f"{ran2} is your number. Will your next be higher or lower?")
                ans = input()
                ran1 = random.randint(1, 15)
                if ans == "Higher" or ans == "higher" and ran1 >= ran2:
                    print(f"{ran1} is your number. Will your next be higher or lower?")
                    ans = input()
            else:
                print(f"{ran2} was your number. You lost.")
                break
    else:
        print("Please use only 'Yes' or 'No'. Capital letters are not needed.")
        pi()
pi()