#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW13

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
fb = 1
while fb <= 99:
    fb += 1
    if fb % 3 == 0 and fb % 5 == 0:
        print("fizzbuzz")
    elif fb % 3 == 0:
        print("fizz")
    elif fb % 5 == 0:
        print("buzz")
    else:
        print(fb)