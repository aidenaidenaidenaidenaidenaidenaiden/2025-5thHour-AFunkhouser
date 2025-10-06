#Name: Aiden Funkhouser
#Class: 5th Hour <-- this said 6th hour how dare you
#Assignment: HW9
import random
#1. Print "Hello World!"
print("Hello World!")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
a = random.randint(1,100), random.randint(1,100), random.randint(1,100)
#3. Print the list.
print(a)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if a[0] >= a[1] and a[0] >= a[2]:
    print(f"{a[0]} Is the biggest number.")
elif a[1] >= a[0] and a[1] >= a[2]:
    print(f"{a[1]} Is the biggest number.")
else:
    print(f"{a[2]} Is the biggest number.")
#5. Tie the result (the largest number) from #4 to a variable called "num".
if a[0] >= a[1] and a[0] >= a[2]:
    num = a[0]
elif a[1] >= a[0] and a[1] >= a[2]:
    num = a[1]
else:
    num = a[2]
#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num % 2 == 0:
    print(f"{num} is even")
elif num % 3 == 0:
    print(f"{num} is divisable by 3")
else:
    print(f"{num} is not divisable by 2 or 3")