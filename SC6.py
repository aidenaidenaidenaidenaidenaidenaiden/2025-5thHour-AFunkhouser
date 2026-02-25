#Name: Aiden Funkhouser
#Class: 5th Hour
#Assignment: Scenario 6

import random

#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Semester Project 1 using classes instead of dictionaries, include and refactor
#the combat test code below as well.)

class party:
    def __init__(self, HP, Init, AC, AtkMod, Damage):
        self.HP = HP
        self.Init = Init
        self.AC = AC
        self.AtkMod = AtkMod
        self.Damage = Damage
class enemy:
    def __init__(self, HP, Init, AC, AtkMod, Damage):
        self.HP = HP
        self.Init = Init
        self.AC = AC
        self.AtkMod = AtkMod
        self.Damage = Damage
LaeZel = party(48, 1, 17, 6,random.randint(1,6) + random.randint(1,6) + 3)
Shadowheart = party(40, 1, 18, 4, random.randint(1,6) + 3,)
Gale = party(32, 1, 14, 6, random.randint(1,10) + random.randint(1,10),)
Astarion = party(40, 3, 14, 5, random.randint(1,8) + random.randint(1,6) + 4,)

Goblin = enemy(7, 0, 12, 4, random.randint(1,6) + 2)
Orc = enemy(15, 1, 13, 5, random.randint(1,12) + 3)
Troll = enemy(84, 1, 15, 7, random.randint(1,6) + random.randint(1,6) + 4)
Mindflayer = enemy(71, 1, 15, 7, random.randint(1,10) + random.randint(1,10) + 4)
Dragon = enemy(127, 2, 18, 7, random.randint(1,10) + random.randint(1,10) + random.randint(1,8) + 4)

initiative1 = random.randint(1,20) + Shadowheart.Init
initiative2 = random.randint(1,20) + Orc.Init

print(f"For initiative, you got {initiative1}, and the enemy got {initiative2}.")
while Shadowheart.HP > 0 and Orc.HP > 0:
    d20 = random.randint(1, 20)
    if initiative1 >= initiative2:
        print("Your turn. You may roll to attack.")
        print(f"You rolled a {d20} for attack, and the enemy has an AC of {Orc.AC}.")
        if d20 + Shadowheart.AtkMod >= Orc.AC and d20 < 20:
            print("The attack lands! You deal some damage.")
            Orc.HP -= random.randint(1, 6) + 3
            print(f"The enemy now has {Orc.HP} health.")
            initiative1 = 1
            initiative2 = 2
        elif d20 == 20:
            print("Critical success! Double damage.")
            Orc.HP -= (random.randint(1, 6) + 3) * 2
            print(f"The enemy now has {Orc.HP} health.")
            initiative1 = 1
            initiative2 = 2
        elif d20 == 1:
            print("Critical failure! Automatic miss.")
            initiative1 = 1
            initiative2 = 2
        else:
            print("The attack misses.")
            initiative1 = 1
            initiative2 = 2
    else:
        print(f"The enemy tries to attack, and gets a {d20}, and your AC is {Shadowheart.AC}.")
        if d20 + Orc.AtkMod >= Shadowheart.AC and d20 < 20:
            print("The enemy succeeds! You take some damage.")
            Shadowheart.HP -= random.randint(1, 12) + 3
            print(f"You now have {Shadowheart.HP} health.")
            initiative1 = 2
            initiative2 = 1
        elif d20 == 20:
            print("Critical success! Double damage.")
            Shadowheart.HP -= (random.randint(1, 12) + 3) * 2
            print(f"You now have {Shadowheart.HP} health.")
            initiative1 = 2
            initiative2 = 1
        elif d20 == 1:
            print("Critical failure! Automatic miss.")
            initiative1 = 2
            initiative2 = 1
        else:
            print("The attack misses.")
            initiative1 = 2
            initiative2 = 1
if Shadowheart.HP <= 0:
    print("You lost...")
elif Orc.HP <= 0:
    print("You won!")