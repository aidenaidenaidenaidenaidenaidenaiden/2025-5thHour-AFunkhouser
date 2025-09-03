#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW4


#1. Print Hello World!
print("Hello World!")
#1. Create a list with 5 strings containing 5 different names in it.
aiden = ["hi im aiden", "tomato sauce", "pi", "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482", "aiden better than sam"]
#2. Append a new name onto the Name List.
aiden.append(input())
#3. Print out the 4th name on the list.
print(aiden[4])
#4. Create a list with 4 different integers in it.
pi = [3.14, 159, 265, 358]
#5. Insert a new integer into the 2nd spot and print the new list.
pi.insert(1, 421)
print(pi)
#6. Sort the list from lowest to highest and print the sorted list.
pi.sort()
print(pi)
#7. Add the 1st three numbers on the sorted list together and print the sum.
pi_subsum = pi[0] + pi[2] + pi[3]
print(pi_subsum)
#8. Create a list with two strings, two variables, and too boolean values.
tomato = ["hi i aiden", "cheddar tomato", 81, 3.141592653589793238, False, True]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(tomato[int(input())])