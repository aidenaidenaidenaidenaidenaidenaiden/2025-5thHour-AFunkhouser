#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW2


#1. Print "Hello World!"
print("Hello World!")

#2. Create three different variables with distinct names and values: one with an integer, one with a string, one with a boolean.
Aiden = 3
Sam = ("tomato cheese its")
Evan = True

#3. Print all three variables on the same print function (at the same time).
print(Aiden, Sam, Evan)

#4. Create a variable that asks the user to input an integer.
intup = int(input())

#5. Add the integer variable from #2 with the integer from #4 and print the result.
answer = Aiden + intup
print(answer)

#6. Take the result from #5 and divide it by 2. Print the result.
print(answer / 2)

#7. Change the value of the boolean variable to the opposite value (if true then make false, or vice versa).
if Evan == True:
    Evan = False
else:
    Evan = True

#8. Print the value of the boolean variable.
print(Evan)

#9. Create a variable with a number that contains decimals.
tomatosauce = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482

#10. Round the number from #9 up or down using the round function.
print(round(tomatosauce))