#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.
pie = [45, 2, 75, 23, 13, 16, 7, 32, 1631]
#2. Sort the list from highest to lowest.
pie.sort()
#3. Create an empty list.
thegame = []
#4. Remove the median number from the first list and add it to the second list.
thegame.append(pie[4])
pie.pop(4)
#5. Remove the first number from the first list and add it to the second list.
thegame.append(pie[0])
pie.pop(0)
#6. Print both lists.
print(pie)
print(thegame)
#7. Add the two numbers in the second list together and print the result.
thegame_subsum = thegame[0] + thegame[1]
print(thegame_subsum)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
pie.append(thegame_subsum)
#9. Sort the first list from lowest to highest and print it.
pie.sort()
print(pie)