#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: HW7

#1. Print Hello World!
print("Hello World!")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
dictionary = {
    "Cheese" : "Cheddar",
    "Pi" : [3, 1, 4],
    "Tomato Sauce" : "Tomato",
}
#3. Print the keys of the dictionary from #2.
print(dictionary.keys())
#4. Print the values of the dictionary from #2
print(dictionary.values())
#5. Print one of the three numbers from the list by itself
print(dictionary["Pi"][0])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
dictionary.update({"Sam" : "Samy Boi"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
flea = {
    "1st_Student" : {
        "Name" : "Dylan",
        "Grade" : 12,
        "Wears Hoodie" : False
    },
    "2nd Student" : {
        "Name" : "Samuel",
        "Grade" : 10,
        "Wears Hoodie" : True
    },
    "3rd Student" : {
        "Name" : "Ivan",
        "Grade" : 12,
        "Wears Hoodie" : False
    },
}
#9. Print the names of all three classmates on the same line.
print(flea["1st_Student"]["Name"],flea["2nd Student"]["Name"],flea["3rd Student"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
flea.pop("2nd Student")
print(flea)