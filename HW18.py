#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
def hw():
    print("Hello World!")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def coinflip():
    global heads, tails
    for i in range(1,101):
        coin = random.randint(1, 2)
        if coin == 1:
            heads += 1
        else:
            tails += 1
#4. Call the "Hello world" and "Coin Flip" functions here
hw()
coinflip()
#5. Print the final result of heads and tails here
print("Heads:", heads)
print("Tails:", tails)
#6. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["Green Bean", "Red Bean", "Blue Bean", "Yellow Bean", "Smaragdine Bean"]
#7. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def randbean():
    random.shuffle(beanBag)
    print(beanBag[0])
    beanBag.remove(beanBag[0])
    ask()
#8. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def ask():
    ans = input("Would you like to pull another bean? ")
    if ans == "yes":
        randbean()
    else:
        print("Ok")
#9. Call the "Bean Pull" function here
randbean()