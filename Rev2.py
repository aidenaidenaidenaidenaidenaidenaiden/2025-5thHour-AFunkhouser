#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW-R2


#1. Print "Hello World!"
print("Hello World!")
#2. Create an empty list.
a = []
#3. Create a list that contains the names of everyone in the classroom.
classroom = ["Dylan", "Ivan", "Brenlyn", "Sam", "Aiden", "Bryson", "Ashton", "Hogan", "Coach Mac"]
#4. Print the list from #3, sort the list, then print the list again.
print(classroom)
list.sort(classroom)
print(classroom)
#5. Append 5 different integers into the empty list from #2 and print the list.
a.append(5)
a.append(10)
a.append(67)
a.append(93)
a.append(42)
print(a)
#6. Add together the middle three numbers in the list from #2 and print the result.
print(a[1]+a[2]+a[3])
#7. Remove the very first number in the list from #2. Print the new first number.
a.pop(0)
print(a[0])
#8. Create a dictionary with three keys with respective values: your name, your grade, and your favorite color.
peoples = {
    "Name" : "Aiden",
    "Grade" : 10,
    "Color" : "Smaragdine"
}
#9. Using the update function, add a fourth key and value determining your favorite candy.
peoples.update({"Candy" : "Chocolate"})
#10. Print ONLY the values of the dictionary from #8.
print(peoples.values())