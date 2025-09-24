#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#It is up to you to decide what properties are important and the theme of the game.
Cool_Enemies = {
    "Ganondorf" : {
        "Health" : 50,
        "Damage Value" : 75,
        "Element" : "Dark"
    },
    "Majora's Mask" : {
        "Health" : 25,
        "Damage Value" : 25,
        "Element" : "None"
    },
    "Sam" : {
        "Health" : 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679,
        "Damage Value" : 0.1,
        "Element" : "Poison (Hoodie)"
    },
    "Demise": {
        "Health": 100,
        "Damage Value": 100,
        "Element": "Dark"
    },
    "Timmy the god destroyer": {
        "Health": 99999999999999,
        "Damage Value": 1000000,
        "Element": "Fire"
    },
}
print(Cool_Enemies["Ganondorf"]["Damage Value"], Cool_Enemies["Majora's Mask"]["Damage Value"], Cool_Enemies["Sam"]["Damage Value"], Cool_Enemies["Demise"]["Damage Value"], Cool_Enemies["Timmy the god destroyer"]["Damage Value"])
Cool_Enemies["Ganondorf"]["Damage Value"] = (int(input()))
Cool_Enemies["Majora's Mask"]["Damage Value"] = (int(input()))
Cool_Enemies["Sam"]["Damage Value"] = (int(input()))
Cool_Enemies["Demise"]["Damage Value"] = (int(input()))
Cool_Enemies["Timmy the god destroyer"]["Damage Value"] = (int(input()))
print(Cool_Enemies["Ganondorf"]["Damage Value"], Cool_Enemies["Majora's Mask"]["Damage Value"], Cool_Enemies["Sam"]["Damage Value"], Cool_Enemies["Demise"]["Damage Value"], Cool_Enemies["Timmy the god destroyer"]["Damage Value"])