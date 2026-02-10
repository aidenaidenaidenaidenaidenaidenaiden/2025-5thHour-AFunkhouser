#Name: Aiden Funkhouser
#Class: 5th Hour
#Assigment: SC4
import random

#After an extended leave, the team lead for the RPG developer is back, and he wants to continue the project.
#He wants to prototype the character creation model but first needs something that rolls stats for the characters.
#He wants you to make a function that rolls 4 six-sided dice (d6), sorts them from highest to lowest, and then adds the
#highest 3 together. He then wants you to add that result to a list outside the function. He wants you to run that function
#5 more times (six times total) and print all six stats.

#Once that is done, to ensure that the average of the statblock is fair (somewhere roughly between 12-13), he wants you
#to plug it into a calculator (SC5) and print the average.

def roll():
    global d6
    d6 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    d6.sort()
roll()
roll1 = d6[1] + d6[2] + d6[3]
roll()
roll2 = d6[1] + d6[2] + d6[3]
roll()
roll3 = d6[1] + d6[2] + d6[3]
roll()
roll4 = d6[1] + d6[2] + d6[3]
roll()
roll5 = d6[1] + d6[2] + d6[3]
roll()
roll6 = d6[1] + d6[2] + d6[3]
stats = [roll1, roll2, roll3, roll4, roll5, roll6]
print(stats)