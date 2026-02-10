#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW19

#1. Import the def functions created in problem 1-4 from HW16
from HW16 import *
#2. Call the functions here and run HW19
hw()
avg(1, 2, 3)
info("axolotl", "bat", "t rex", "gorilla", "giraffe")
number(int(input("Enter the number: ")))
#3. Delete all calls from HW16 and run HW19 again.
# They're gone. Reduced to atoms.
#4. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(pi)
except:
    print("Hello World!")
#5. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    num_div = int(input("Give me an integer: "))
    print(100/num_div)
except:
    print("NO DO NEVER DIVIDE BY WITH 0")
#6. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    k = int(input("Give me an integer"))
    print(k)
except:
    print("It needs to be an integer!")
#7. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
tomatosauce = 5
while True:
    tomatosauce -= 1
    print(tomatosauce)
    if tomatosauce < 0:
        raise Exception("tomatosauce cannot be negative!")