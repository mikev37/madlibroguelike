import random
import math
#translation not original code
class Weapon:
    #there were a bunch of class variables here, but I am pretty sure they want to be instance attributes instead
    #maybe desc would be a good class variable candidate but doubtful if it wants to be different for each weapon?
    def __init__(self):  #this runs for every instance???
        self.x = random.randint(1, 400)
        self.y = random.randint(1, 400)
        self.bonus = random.randint(1, 3)
        self.spread = random.randint(0, 5)
        self.uses = random.randint(1, 6)
        self.rng = random.randint(1, 6)
        self.desc = "" #i made the description an instance variable

        f = open('adjectives.txt', 'r') #opens adj.txt in read mode
        arr = [] #empty list for appending?

        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0, len(arr)-1)][0:-1]
        f.close()

        f = open('weapons.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0, len(arr)-1)][0:-1]
        f.close()

    def effect(self, player):
        player.weapon.append(self)
        self.x = 90001

    def description(self):
        return self.desc + "\n Damage: " + str(self.bonus) + "-" + str(self.spread+self.bonus) + " Range: " + str(self.rng) + " Condition: " + str(self.uses) + "\n"

    def breakStuff(self):
        print("Your" + self.desc + " breaks :[")
        self.bonus = 0

    def attack(self, mon):
        atk = self.bonus + random.randint(0, self.spread)
        self.uses = self.uses - 1
        mon.hp = mon.hp-atk
        print("You hit the " + mon.desc + " with your " + self.desc + " for " + str(atk) + " Damage!")


##TEST ARENA
Weapon1 = Weapon()
print(Weapon1.desc)
Weapon.description(Weapon1)
print(Weapon.description(Weapon1))
