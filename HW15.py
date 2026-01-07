#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("Give a number   "))
b = int(input("Give another number  "))
c = int(input("Give another number  "))
#4. Add a and b together, then divide the sum by c. Print the result.
d = round((a + b) / c)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(d)
if d % 2 == 0:
    print("The number is even")
if d % 2 == 1:
    print("The number is odd")
#6. Create a list of five different random integers between 1 and 10.
list = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
#7. Print the 4th number in the list.
print(list[3]) #0 is 1
#8. Append another integer to the end of the list, also random from 1 to 10.
e = random.randint(1, 10)
list.insert(5, e)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
list.sort()
print(list[3])
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i < 102: #this is to let i be greater than 100
    print(i)
    i += 1
#11. Create a list containing the names of five other students in the classroom.
classlist = ["Dylan", "Ivan", "Sam", "Aiden", "Hogan"]
#12. Create a for loop that individually prints out the names of each student in the list.
for x in classlist:
    print(x)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for w in range(1, 101):
    print(w)
    if w % 10 == 0:
        break
#14. Free space. Do something creative. :)
# Rock Paper Scissors!!!
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