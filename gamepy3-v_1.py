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

class Player:
    x = 200
    y = 200
    startinghp = 10
    maxhp = 10
    rng = 2
    speed = 2
    atk = 1
    desc = ""
    gold = 0
    level = 1
    exp = 0
    maxXP = 2
    weapon = []

    def description(self):
        desc = "You are level " + str(self.level) + " " + self.desc + "\n Carrying :"
        for w in self.weapon:
            desc = desc + w.description()
        desc = desc + " and " + str(self.gold) + " Gold Dulboons!"
        return desc

    def endTurn(self):
        if(self.exp >= self.maxXP):
            self.levelUp()
        for w in self.weapon:
            if(w.uses <= 0):
                w.breakStuff()
                self.weapon.remove(w)
            
    def see(self, mon):
        rng = self.rng
        for w in self.weapon :
            pass
    
##TEST ARENA
Play1 = Player()
Weapon1 = Weapon()
print(Weapon1.desc)
Weapon.description(Weapon1)
print(Weapon.description(Weapon1))
print(Player.description(Play1))
