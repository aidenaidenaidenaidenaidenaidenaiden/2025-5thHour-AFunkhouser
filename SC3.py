#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all the ratings.
avg = []
while 1 < 2:
    a = int(input("How many players do you want?    "))
    if a <= 0:
        print("Please choose a number above 0.")
    elif a >= 1:
        for i in range(a):
            print("player")
            c = int(input("What would you rate this player?    "))
            if c <= 0 or c >= 6:
                print("Please choose a number above 0 and below 6.")
            elif c < 6 or c > 0:
                avg.append(c)
            else:
                print("Please choose a number.")
    else:
        print("Please choose a number. A number is a digit such as 1, 2, 3, etc. my favorite example is 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
    pi = sum(avg)
    print(pi / a)
    break