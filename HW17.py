#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW17
import random

#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

def rps(p1):
    p2 = random.randint(1, 3)
    if p1 == p2:
        print("Draw!")
    elif p1 == 2 and p2 == 1 or p1 == 1 and p2 == 3 or p1 == 3 and p2 == 2:
        print("You win.")
    else:
        print("You lose.")
    end()

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
def end():
    print("Would you like to play again?")
    again = input()
    if again == "y":
        rps(p1 = int(input("rock = 1, paper = 2, scissors = 3. Choose one. ")))
    else:
        exit()
rps(p1 = int(input("rock = 1, paper = 2, scissors = 3. Choose one. ")))