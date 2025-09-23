print("Before we start do you wanna see Pi?")
print("Type 'Yes' or 'No' to continue.")
a = input()
if a == 'Yes':
    print("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482.")
#Begin asking the player their name, then what to do and how to do that action.
from fileinput import close
if a == "No":
    print("What's your name?")
    name = input()
    print(f"Welcome {name}!")
    print("You're starting your adventure. You're standing on the edge of a cliff, off a big plateau.")
    print("From the cliff, you can see a giant tower glowing orange. There is 4 large shrines somewhat near the tower, also glowing orange.")
    print("Will you explore the tower or the shrines?")
    print("Type 'Tower' or 'Shrines' to continue.")
#When selecting Shrines
    a = input()
    if a == "Shrines":
        print("The shrine you visit is locked. You should really check the Tower first.")
        print("Type 'Tower' or 'Shrines' to continue.")
        a = input()
        if a == "Shrines":
            print("You've visited the shrines. You should really check the Tower first.")
            print("Type 'Tower' or 'Shrines' to continue.")
            a = input()
            if a == "Shrines":
                print("Dude stop. Don't type that again.")
                print("Type 'Tower' or 'Tower' to continue.")
                a = input()
                if a == "Shrines":
                    print("STOPPPPP. WHY DONT YOU LISTENNNNNN??????")
                    print("Type 'Tower' to continue.")
                    a = input()
                    if a == "Shrines":
                        print("That's it. No more game.")
                        print("Type absolutely nothing to continue.")
                        exit()
#this is for selecting "Tower"
    if a == "Tower":
        print("The tower is very tall, it might hurt a bit to fall from it.")
        print("Would you like to climb it?")
        print("Type 'Yes' or 'No' to continue.")
        a = input()
        if a == "No":
            print("But theres nothing else to do. Just climb it.")
            print("Type 'Yes' to continue.")
            a = input()
        if a == "Yes":
            print("You climb it and see stuff. You now have access to the Shrines.")
            print("Type 'Shrines' to continue.")
            a = input()
        if a == "Shrines":
            print("Congrats, you have access to the Shrines. You may complete the Shrines. Do you want to?")
            print("Type 'Yes' or 'No' to continue.")
            a = input()
            if a == "No":
                print("Do it.")
                print("Type 'Yes' to continue.")
                a = input()
            if a == "Yes":
                print("You beat the shrines. Do you wish to go to the temple?")
                print("Type 'Yes' or 'No' to continue.")
                a = input()
                if a == "No":
                    print("You have no option.")
                    print("Type 'Yes' or 'Yes' to continue.")
                    a = input()
                    if a == "No":
                        print("DO ITTTTTTTTT.")
                        print("Type 'Yes' to continue.")
                        a = input()

            if a == "Yes":
                print("Good. You've beat the game.")
                print("Type 'What's the game?' to continue.")
                a = input()
                if a == "What's the game?":
                    print("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA.")
                if a == "No":
                    print("HOW DARE YOUUUUUUUUUU")
                if a == "Pi":
                    from mpmath import mp
                    mp.dps = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                    print(mp.pi)