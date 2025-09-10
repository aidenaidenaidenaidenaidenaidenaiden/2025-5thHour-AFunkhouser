#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW6


#1. Import the "random" library
import random

#2. print "Hello World!"
print("Hello World!")

#3. Create three different variables that each randomly generate an integer between 1 and 10
thegame = random.randint(1,10)
tomato = random.randint(1,10)
cheese = random.randint(1,10)

#4. Print the three variables from #3 on the same line.
print(thegame, tomato, cheese)

#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
thegame += 2
tomato -=4
cheese *= 1.5

#6. Print each result from #5 on the same line.
print(thegame, tomato, cheese)

#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
aiden = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]

#8. Sort the list in #7 and print it.
aiden.sort()
print(aiden)

#9. Add together the highest three numbers in the list from #7 and print the result.
aiden.pop(0)
aiden_subsum = aiden[0] + aiden[1] + aiden[2]
print(aiden_subsum)

#10. Create a list with 5 names of other students in this class and print the list.
pi = ["Sam", "Ivan", "Hogan", "Brenlyn", "Tristan"]
print(pi)

#11. Shuffle the list in #10 and print the list again.
random.shuffle(pi)
print(pi)

#12. Print a random choice from the list of names from #10.
print(pi[0])