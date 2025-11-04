#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW12

#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
import random
i = 5
while i > 0:
    print(i)
    i -= 1
else:
    print("Hello World!")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
a = 1
while a < 30:
    a = a + 1
    if a % 2 == 0:
        print(a)
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the number is divisible by 3.
b = 1
while b < 30:
    b = b + 1
    if b % 3 == 0:
        continue
    else:
        print(b)
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
c = random.randint(1,6)
while c > 0:
    print(c)
    if c == 1:
        break
    else:
        c = random.randint(1,6)
#5. Create a while loop that asks for a number input until the user inputs the number 0.
d = int(input())
while d > 0:
    d = int(input())
else:
    print(d)