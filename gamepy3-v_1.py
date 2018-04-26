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
        arr = [] #empty list for appending
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0, len(arr)-1)][0:-1] #WHAT ARE YOU DOING
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

class Item:
    def __init__(self):
        self.x = random.randint(1, 400)
        self.y = random.randint(1, 400)
        self.case = random.randint(1, 3)
        self.desc = ""
        self.verb = ""
        self.gold = 0 #as with before moved class variables to instance variables. initialized at 0
        self.hpBonus = 0
        self.xpBonus = 0
        
        if self.case == 1 :
            self.hpBonus = random.randint(1 ,3)
        elif self.case == 2 :
            self.xpBonus = random.randint(1, 3)
        elif self.case == 3 :
            self.gold = random.randint(100, 300)

        f = open('adjectives.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0, len(arr) -1)][0: -1]
        f.close()

        f = open('nouns.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0, len(arr) -1)][0: -1]
        f.close()

        f = open('verbs.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.verb = self.verb + arr[random.randint(0, len(arr) -1)][0: -1]
        f.close()

    def effect(self, player):
        player.hp = min(player.maxHP,player.hp + self.hpBonus)
        player.exp = player.exp + self.xpBonus
        player.gold = player.gold + self.gold
        self.x = 90001

    def description(self):

        if self.case == 1 :
            return "You " + self.verb + " a " + self.desc + "\n Heal " + str(self.hpBonus) + " Health"
        elif self.case == 2 :
            return "You " + self.verb + " a " + self.desc + "\n Gain " + str(self.xpBonus) + " Experience points"
        elif self.case == 3 :
            return "You find " + str(self.gold) + "Gold under a \n" + self.desc

class Player:
#left class variables here as there will only ever be one player
    x = 200
    y = 200
    hp = 10
    maxHP= 10
    rng = 2
    speed = 2
    atk = 1
    desc = ""
    gold = 0
    level = 1
    exp = 0
    maxXP = 2
    weapon = []

    def __init__(self):
        self.desc = "adventurer(s)"

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
            if(math.hypot(mon.x - player.x, mon.y - player.y) < w.rng):
                w.attack(mon)
        if(math.hypot(mon.x - player.x, mon.y - player.y) < w.rng):
            self.fight(mon)
        if(mon.hp <= 0 and mon.x<400): #why is the second part here
            self.kill(mon)

    def fight(self, mon):
        atk = self.atk + random.randint(0,2)
        f = open('verbs.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        print("you " + arr[random.randint(0,len(arr)-1)][0 : -1] + " the " + mon.desc + " for " + str(atk) + " Damage")
        f.close()
        mon.hp = mon.hp - atk

    def kill(self, monster): #why passing monster instead of mon hmmm
        self.exp = self.exp + monster.level
        monster.x = 90001
        print("You kill the " + monster.desc)

    def levelUp(self):
        print("You leveled up! ")
        self.exp = 0
        self.maxXP = self.maxXP * 2
        self.level = self.level + 1
        case = random.randint(1, 4)
        if(case == 1):
            self.rng = self.rng + 1
        elif(case == 2):
            self.atk = self.atk + 1
        elif(case == 3):
            self.speed = self.speed + 1
        elif(case == 4):
            self.speed = self.speed + 4
        self.maxHP = self.maxHP + 1
        self.hp = self.maxHP

class Monster:
    #again, several class variables were here, I don't think they are wanted
    def __init__(self, level, x, y):
        #instance attributes
        self.level = level
        self.x = x
        self.y = y
        self.hp = level * random.randint(1, 3)
        self.atk = level + random.randint(-1 , 2)
        self.desc = ""
        self.strike = ""

        f = open('verbs.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.strike = self.strike + arr[random.randint(0, len(arr) -1)][0 : -1] + "s you with it's "
        f.close()

        f = open('adjectives.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        for i in range(level):
            self.desc = self.desc + arr[random.randint(0, len(arr) -1)][0 : -1] + " "
            self.strike = self.strike + arr[random.randint(0, len(arr) -1)][0 : -1] + " "
        f.close

        f = open('monsters.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0, len(arr) -1)][0 : -1]
        f.close()

        f = open('nouns.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.strike = self.strike + arr[random.randint(0, len(arr) -1)]#[0 : -1]
        f.close()
           
    def description(self):
        return self.desc + " at " + str(self.hp) + " Health"


#DRAW FUNCTIONS
def draw(world, x, y, monsters):
    size = 20 #size changed from 11 to 12 and suddenly the player indicator works
    for i in range(-1, size + 2):
        for c in range(-1,  size + 2):
            if i == -1 or i == size + 1 :
                print('=', end = ' ')
            elif c == -1 or c == size + 1 :
                print('|', end = ' ')
            elif c == size / 2 and i == size / 2 :
                print('X', end = ' ')
            else :
                flag = True
                for m in monsters :
                    if(i + x - size/2 == m.x and c + y - size/2 == m.y):
                        print(mon(m.level), end = ' ')
                        flag = False
                for t in treasure :
                    if (int(i + x - size/2) == m.x and int(c + y - size/2) == t.y):
                        print('t', end = ' ')
                        flag = False
                for t in arsenal :
                    if (int(i + x - size/2) == m.x and int(c + y - size/2) == t.y):
                        print('t', end = ' ')
                        flag = False
                if (flag): #original code 'if(flag):'
                    print(f(world[x + i - int(size/2)][y + c - int(size/2)]), end = ' ') #there are commas at the end of py2 to end print w/o a newline
        if i == 0 :
            print("Health: ",player.hp,"/",player.maxHP)
        elif i == 1 :
            print("EXP: ",player.exp,"/",player.maxXP)
        elif i == 2 :
            print("STR: ",player.atk)
        elif i == 3 :
            print("SPD: ",player.speed)
        elif i == 4 :
            print("RNG: ",player.rng)
        else:
            print("")

def points(world):
    for i in range(0, len(world[0]), 10):
        for c in range(5, len(world[0])-5, 5):
            world[i][c] = random.randint(1, 6)
    return world

def midrange(world):
    for i in range(5,len(world)-5,5):
        for c in range(5,len(world[0])-5,5) :
            if(world[i][c] == 0):
                world[i][c] = (world[i-5][c] + world[i+5][c] + world[i][c+5] + world[i][c-5])/4+random.randint(1,6)
    return world

def fillOutLine(world):
    for i in range(0,len(world),5):
        for c in range(len(world[0])-5) :
            if(world[i][c] == 0):
                world[i][c] = interpol(world[i][int(c/5*5)],world[i][int(c/5*5+5)],int((c%5)/5.0))
    return world

def fillOut(world):
    for i in range(0, len(world) - 5):
        for c in range(len(world[0]) - 5) :
            if(world[i][c] == 0):
                world[i][c] = interpol(world[int(i/5*5)][c], world[int(i/5*5+5)][c], int((i%5)/5.0))
            if(i > 190 and i < 210 and c > 190 and c < 210):
                world[i][c] = 0
    return world

def interpol(a, b, f):
    return int(a * (1 - f) + b * (f))

#dictionary functions
def f(x):
    return {
        -1 : ' ',
        0  : ' ',
        1  : ' ',
        2  : ' ',
        3  : ' ',
        4  : ' ',
        5  : ' ',
        6  : 'O',
        7  : 'O',
    }.get(x, 'O')

def mon(x):
    return {
        1  : 'm',
        2  : 'w',
        3  : 'M',
    }.get(x, 'W')

#GLOBAL VARIABLES
mybigness = 401 #should b 401 left as 10 for testing purposed
world = [[0 for i in range(mybigness)] for i in range(mybigness)] 
monsters = []
treasure = []
arsenal = []
#player = Player()

#RUN FUNCTIONS (also global)
def start(level):
    world = [[0 for i in range(mybigness)] for i in range(mybigness)] #i think i see an incomaptability here maybe 
    world = points(world)
    world = midrange(world)
    world = fillOutLine(world)
    world = fillOut(world)
    monsters = populate(400)
    treasure = scatter(200)
    arsenal = weaponize(200)
    return world, monsters, treasure, arsenal
    
def boot():
    global player
    player = Player()
    start(1)
    
#POPULATION FUNCTIONS
def populate(num):
    monsters = []
    for i in range(num):
        monsters.append(Monster(random.randint(1,4),random.randint(0, mybigness - 1), random.randint(0, mybigness - 1)))
    return monsters

def scatter(num):
    treasure = []
    for i in range(num):
        treasure.append(Item())
    return treasure

def weaponize(num):
    arsenal = [] #this confusing? supposed to be arsenal?
    for i in range(num):
        arsenal.append(Weapon())
    return arsenal

#GAME IN FUNCTIONS
def inventory():
    print( player.description() )

def look():
    print("It's dark...")
    for mon in monsters :
        if(math.hypot(mon.x - player.x, mon.y - player.y) < 10):
            print("You see a " + mon.desc)
    for mon in treasure :
        if(math.hypot(mon.x - player.x, mon.y - player.y) < 10):
            print("You see a " + mon.desc)
    for mon in arsenal :
        if(math.hypot(mon.x - player.x, mon.y - player.y) < 10):
            print("You see a " + mon.desc)

def turn():
    for mon in monsters :
        mon.x = mon.x + random.randint(-mon.level, mon.level)
        mon.y = mon.y + random.randint(-mon.level, mon.level)
        player.see(mon)
        if(math.hypot(mon.x - player.x, mon.y - player.y) < mon.level * 1.1):
            print(mon.desc + " " + mon.strike)
            player.hp = player.hp - mon.atk

    for mon in treasure :
        if math.hypot(mon.x - player.x, mon.y - player.y) < 2:
            print(mon.description())
            mon.effect(player)
            treasure.remove(mon)

    for mon in arsenal :
        if (math.hypot(mon.x - player.x, mon.y - player.y) < 2):
            print("You pick up a " + mon.desc)
            mon.effect(player)
            arsenal.remove(mon)

def shuffle(dx, dy):
    drx = 0
    dry = 0
    if (dx > 0):
        drx = int(math.ceil(dx*1.0/10.0))
    else:
        drx = int(math.ceil(dx*1.0/10.0))
    if (dy > 0):
        dry = int(math.ceil(dy*1.0/10.0))
    else:
        dry = int(math.floor(dy*1.0/10.0))
    if(drx != 0):
        for i in range(0, dx, drx):
            if(f(world[player.x + drx][player.y]) != 'O'):
                player.x = player.x + drx
    turn()
    draw(world, player.x, player.y, monsters)
    player.endTurn()

def move():
    flag = True
    draw(world, player.x, player.y, monsters)
    while (flag):
        walk = input("Where to go (NESW) or LOOK or INV or QUIT:   ")

        if(walk[0] == "W"):
            if(len(walk) > 1):
                dist = min(int(walk[-1]), player.speed)
                shuffle(0, -dist)
            else: shuffle(0, -player.speed)

        elif(walk[0] == "S"):
            if(len(walk) > 1):
                dist = min(int(walk[-1]), player.speed)
                shuffle(0, -dist)
            else: shuffle(0, -player.speed)

        elif(walk[0] == "E"):
            if(len(walk) > 1):
                dist = min(int(walk[-1]), player.speed)
                shuffle(0, -dist)
            else: shuffle(0, -player.speed)

        elif(walk[0] == "N"):
            if(len(walk) > 1):
                dist = min(int(walk[-1]), player.speed)
                shuffle(0, -dist)
            else: shuffle(0, -player.speed)

        elif(walk == "INV"):
            inventory()
        elif(walk == "LOOK"):
            look()
        elif(walk == "QUIT"):
            flag = False
        else:
            print("Command not recognized")

        if(player.hp <= 0):
            print("You died. You got to level " + str(player.level) + " and had " + str(player.gold) + " Gold")
            flag = False
            
##TEST ARENA
boot()
move()
            #look() and look work in shell as does inventory()
##Play1 = Player()
##Weapon1 = Weapon()
##print(Weapon1.desc)
##Weapon.description(Weapon1)
##print(Weapon.description(Weapon1))
##print(Player.description(Play1))
##print(Weapon.breakStuff(Weapon1))
##Item1 = Item()
##print(Item1.desc + Item.description(Item1))
##monster1 = Monster(random.randint(1,4),random.randint(0,400),random.randint(0,400))
##print(monster1.desc)
## draw() works now should shortly be playable game :)
##player = Player()
##world = points(world)
##draw(world, player.x, player.y, monsters)
##world = midrange(world)
##world = fillOutLine(world)
##world = fillOut(world)
##monsters = populate(400)
##treasure = scatter(400)
##arsenal = weaponize(200)
##
##draw(world, player.x, player.y, monsters)
