#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW16
import random

#1. Create a def function that prints out "Hello World!"
def hw():
    print("Hello World!")
#2. Create a def function that calculates the average of three numbers (set the 3 numbers as your arguments).
def avg(a, b, c):
    d = (a + b + c) / 3
    print("The average is: ", d)
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def info(*animalinfo):
    print("The 3rd animal is", animalinfo[2])
#4. Create a def function that loops from 1 to the number put in the argument.
def number(num):
    for i in range (1, num + 1):
        print(i)
#5. Call all the functions created in 1 - 4 with relevant arguments.
hw()
avg(1, 2, 3)
info("axolotl", "bat", "t rex", "gorilla", "giraffe")
number(int(input("Enter the number: ")))
#6. Create a variable x that has the value of 2. Print x
x = 2
print(x)
#7. Create a def function that multiplies the value of 2 by a random number between 1 and 5.
def mul(no1, no2):
    res = no1 * no2
    print("The result is: ", res)
mul(2, random.randint(1, 5))
#8. Print the new value of x.
#done in 7 :)