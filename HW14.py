#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW14


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5,0,-1):
    print(i)
else:
    print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for a in range(1,31):
    if a % 2 == 0:
        print(a)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for b in range(1,31):
    if b % 3 == 0:
        continue
    else:
        print(b)
#4. Create a for loop that prints 5 different animals from a list.
list = ["Axolotl", "Dog", "Cat", "Monkey", "Donkey (from Shrek)"]
for c in list:
    print(c)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for c in input("Enter a word: ")[::-1]:
    print(c)
#6. Create a list containing 10 integers of your choice and print the list.
intlist = [3, 1415, 9265, 3589, 7932, 3846, 2643, 3832, 7950, 2884]
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = ()
oddNumbers = ()
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for n in intlist:
    if n % 2 == 0:
        evenNumbers += (n,)
    elif n % 2 == 1:
        oddNumbers += (n,)
e = 0
o = 0
for n in evenNumbers:
    e += 1
print(f"The amount of even numbers is: {e}")
for n in oddNumbers:
    o += 1
print(f"The amount of odd numbers is: {o}")
#9. Create a variable that asks the user for an integer and an empty integer variable.
cheese = int(input("Enter a number: "))
pi = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for i in range(1, cheese + 1):
    pi *= i
print(pi)