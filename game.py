
import random
import math


class Weapon:
    x = 0
    y = 0
    spread = 0
    bonus = 0
    uses = 0
    rng = 0
    desc = ""
    def __init__(self):
        self.x =  random.randint(1,400)
        self.y =  random.randint(1,400)
        self.bonus = random.randint(1,3)
        self.spread = random.randint(0,5)
        self.uses = random.randint(1,6)
        self.rng = random.randint(1,6)
        
        f = open('adjectives.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0,len(arr)-1)][0:-1]
        f.close()
        f = open('weapons.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0,len(arr)-1)][0:-1]
        f.close()


    def effect(self,player):
        player.weapon.append(self)
        self.x = 90001
        
    def description(self):
        return self.desc + "\n Damage: "+str(self.bonus)+"-"+str(self.spread+self.bonus)+" Range: "+str(self.rng)+" Condition: "+str(self.uses)+"\n"

    def breakStuff(self):
        print( "Your "+self.desc+ " breaks")
        self.bonus = 0

    def attack(self,mon):
        atk = self.bonus + random.randint(0,self.spread)
        self.uses = self.uses - 1
        print( "You hit the "+mon.desc+" with your "+self.desc+" for "+str(atk)+" Damage")

class Item:
    x = 0
    y = 0
    xpBonus = 0
    hpBonus = 0
    gold = 0
    case = 0
    desc = ""
    verb = ""
    def __init__(self):
        self.x =  random.randint(1,400)
        self.y =  random.randint(1,400)
        self.case = random.randint(1,3)
        if(self.case == 1):
            self.hpBonus = random.randint(1,3)
        elif(self.case == 2):
            self.xpBonus = random.randint(1,3)
        elif(self.case == 3):
            self.gold = random.randint(100,300)
        f = open('adjectives.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0,len(arr)-1)][0:-1]
        f.close()
        f = open('nouns.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0,len(arr)-1)][0:-1]
        f.close()
        f = open('verbs.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.verb = self.verb + arr[random.randint(0,len(arr)-1)][0:-1]
        f.close()

    def effect(self,player):
        player.hp = min(player.maxHP,player.hp + self.hpBonus)
        player.exp = player.exp + self.xpBonus
        player.gold = player.gold + self.gold
        self.x = 90001
    
    def description(self):
        
        if(self.case == 1):
            return "You "+self.verb+" a "+self.desc+"\n Heal "+str(self.hpBonus)+" Health"
        elif(self.case == 2):
            return "You "+self.verb+" a "+self.desc+"\n Gain "+str(self.xpBonus)+" Expierience points"
        elif(self.case == 3):
            return "You find "+str(self.gold)+" Gold under a \n"+self.desc

class Monster:
    x = 0
    y = 0
    hp = 1
    level = 1
    atk = 1
    desc = ""
    strike = ""

    def description(self):
        return self.desc + " at "+str(self.hp)+" Health"
    
    def __init__(self,level,x,y):
        self.level = level
        self.x = x
        self.y = y
        self.hp = level*random.randint(1,3)
        self.atk = level+random.randint(-1,2)
        f = open('verbs.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.strike = self.strike + arr[random.randint(0,len(arr)-1)][0:-1] + "s you with its "
        f.close()
        f = open('adjectives.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        for i in range(level):
            self.desc = self.desc + arr[random.randint(0,len(arr)-1)][0:-1] +" "
            self.strike = self.strike + arr[random.randint(0,len(arr)-1)][0:-1]+" "
        f.close()
        f = open('monsters.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.desc = self.desc + arr[random.randint(0,len(arr)-1)][0:-1]
        f.close()
        f = open('nouns.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        self.strike = self.strike + arr[random.randint(0,len(arr)-1)][0:-1]
        f.close()


class Player:
    x = 200
    y = 200
    hp = 10
    maxHP = 10
    rng = 2
    speed = 2
    atk = 1
    desc = ""
    gold = 0
    level = 1
    exp = 0
    maXP = 2
    weapon = []
    def description(self):
        desc = "You are a level "+str(self.level)+" "+self.desc+"\n Carrying :"
        for w in self.weapon:
            desc = desc + w.description()
        desc = desc + " and "+str(self.gold)+" Gold Dubloons"
        return desc

    def endTurn(self):
        if(self.exp >= self.maXP):
            self.levelUp()
        for w in self.weapon:
            if(w.uses <= 0):
                w.breakStuff()
                self.weapon.remove(w)

    def see(self,mon):
        rng = self.rng
        for w in self.weapon :
            if(math.hypot(mon.x - player.x, mon.y - player.y)<w.rng):
                w.attack(mon)
        if(math.hypot(mon.x - player.x, mon.y - player.y)<self.rng):
            self.fight(mon)
        if(mon.hp<=0 and mon.x<400):
            self.kill(mon)

    def fight(self,mon):
        atk = self.atk + random.randint(0,2)
        f = open('verbs.txt', 'r')
        arr = []
        for line in f :
            line.strip()
            arr.append(line)
        print("you "+arr[random.randint(0,len(arr)-1)][0:-1]+" the "+mon.desc+" for "+str(atk)+" Damage")
        f.close()
        mon.hp = mon.hp - atk

    def kill(self,monster):
        self.exp = self.exp + monster.level
        monster.x = 90001
        print("You kill the "+monster.desc)

    def levelUp(self):
        print("You leveled up!")
        self.exp = 0
        self.maXP = self.maXP * 2
        self.level = self.level + 1
        case = random.randint(1,3)
        if(case == 1):
            self.rng = self.rng + 1
        elif(case == 2):
            self.atk = self.atk + 1
            self.maxHP = self.maxHP + 1
        elif(case == 3):
            self.speed = self.speed + 1
        self.hp = self.maxHP
    
    def __init__(self):
        self.desc = "adventurer"

def draw(world,x,y,monsters):
    size = 11
    for i in range(-1,size+2):
        for c in range(-1,size+2) :
            if i == -1 or i == size+1 :
                print ('='),
            elif c == -1 or c == size+1 :
                print ('|'),
            elif c == size/2 and i == size/2 :
                print ('X'),
            else :
                flag = True
                for m in monsters :
                    if(i+x-size/2 == m.x and c+y-size/2 == m.y):
                        print(mon(m.level)),
                        flag = False
                for t in treasure :
                    if(i+x-size/2 == t.x and c+y-size/2 == t.y):
                        print('t'),
                        flag = False
                for t in arsenal :
                    if(i+x-size/2 == t.x and c+y-size/2 == t.y):
                        print('t'),
                        flag = False               
                if(flag):
                    print(f(world[x+i-size/2][y+c-size/2])),
        if( i == 0):
            print "health:",player.hp,"/",player.maxHP
        elif(i == 1):
            print "EXP:",player.exp,"/",player.maXP
        elif(i == 2):
            print "STR:",player.atk
        elif(i == 3):
            print "SPD:",player.speed
        elif(i == 4):
            print "RNG:",player.rng
        else:
            print("")

def points(world):
    for i in range(0,len(world),10):
        for c in range(0,len(world[0]),10) :
            world[i][c] = random.randint(1,6)
    return world

def midrange(world):
    for i in range(5,len(world)-5,5):
        for c in range(5,len(world[0])-5,5) :
            if(world[i][c] == 0):
                world[i][c] = (world[i-5][c]+world[i+5][c]+world[i][c+5]+world[i][c-5])/4+random.randint(1,6)
    return world

def fillOutLine(world):
    for i in range(0,len(world),5):
        for c in range(len(world[0])-5) :
            if(world[i][c] == 0):
                world[i][c] = interpol(world[i][c/5*5],world[i][c/5*5+5],(c%5)/5.0)
    return world

def fillOut(world):
    for i in range(0,len(world)-5):
        for c in range(len(world[0])-5) :
            if(world[i][c] == 0):
                world[i][c] = interpol(world[i/5*5][c],world[i/5*5+5][c],(i%5)/5.0)
            if(i > 190 and i < 210 and c > 190 and c < 210):
                world[i][c] = 0
    return world

def interpol(a,b,f):
    return int(a*(1-f)+b*(f))#+random.randint(-1,1)

def populate(num):
    monsters = []
    for i in range(num):
        monsters.append(Monster(random.randint(1,4),random.randint(0,400),random.randint(0,400)))
    return monsters

def scatter(num):
    treasure = []
    for i in range(num):
        treasure.append(Item())
    return treasure

def weaponize(num):
    treasure = []
    for i in range(num):
        treasure.append(Weapon())
    return treasure

def mon(x):
    return {
        1  : 'm',
        2  : 'w',
        3  : 'M',
    }.get(x, 'W') 

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
world = [[0 for i in range(401)] for i in range(401)]
monsters = []
treasure = []
arsenal = []
player = Player()
def start(level):
    world = [[0 for i in range(401)] for i in range(401)] 
    world = points(world)
    world = midrange(world)
    world = fillOutLine(world)
    world = fillOut(world)
    monsters = populate(400)
    treasure = scatter(400)
    arsenal = weaponize(200)
    
world = points(world)
world = midrange(world)
world = fillOutLine(world)
world = fillOut(world)
monsters = populate(400)
treasure = scatter(400)
arsenal = weaponize(200)
def boot():
    player = Player()
    start(1)

def inventory():
    print ( player.description() )

def look():
    print ( "It's dark")
    for mon in monsters :
        if(math.hypot(mon.x - player.x, mon.y - player.y)<10):
           print("You see a "+mon.description())
    for mon in treasure :
        if(math.hypot(mon.x - player.x, mon.y - player.y)<10):
           print("You see a "+mon.desc)
    for mon in arsenal :
        if(math.hypot(mon.x - player.x, mon.y - player.y)<10):
            print("You see a "+mon.desc)
           
def turn():
    for mon in monsters :
        mon.x = mon.x + random.randint(-mon.level,mon.level)
        mon.y = mon.y + random.randint(-mon.level,mon.level)
        player.see(mon)
        if(math.hypot(mon.x - player.x, mon.y - player.y)<mon.level*1.1):
            print(mon.desc + " "+ mon.strike)
            player.hp = player.hp - mon.atk

    for mon in treasure :
        if(math.hypot(mon.x - player.x, mon.y - player.y)<2):
            print(mon.description())
            mon.effect(player)
            treasure.remove(mon)
    for mon in arsenal :
        if(math.hypot(mon.x - player.x, mon.y - player.y)<2):
            print("You pick up a "+mon.desc)
            mon.effect(player)
            arsenal.remove(mon)

def shuffle(dx,dy):
    drx = 0
    dry = 0
    if(dx > 0):
        drx = int(math.ceil(dx*1.0/10.0))
    else:
        drx = int(math.floor(dx*1.0/10.0))
    if(dy > 0):
        dry = int(math.ceil(dy*1.0/10.0))
    else:
        dry = int(math.floor(dy*1.0/10.0))
    if(drx!=0):
        for i in range(0,dx,drx):
            if(f(world[player.x+drx][player.y])!='O'):
                player.x = player.x + drx
    if(dry!=0):           
        for i in range(0,dy,dry):
            if(f(world[player.x][player.y+dry])!='O'):
                player.y = player.y + dry
    turn()
    draw(world,player.x,player.y,monsters)
    player.endTurn()

def move():
    flag = True
    draw(world,player.x,player.y,monsters)
    while(flag):
        walk = raw_input('Where to go (NESW) or LOOK or INV or QUIT:  ')
        if(walk[0] == "W"):
            if(len(walk)>1):
                dist = min(int(walk[-1]),player.speed)
                shuffle(0,-dist)
            else: shuffle(0,-player.speed)
        elif(walk[0] == "S"):
            if(len(walk)>1):
                dist = min(int(walk[-1]),player.speed)
                shuffle(dist,0)
            else: shuffle(player.speed,0)
        elif(walk[0] == "E"):
            if(len(walk)>1):
                dist = min(int(walk[-1]),player.speed)
                shuffle(0,dist)
            else: shuffle(0,player.speed)
        elif(walk[0] == "N"):
            if(len(walk)>1):
                dist = min(int(walk[-1]),player.speed)
                shuffle(-dist,0)
            else: shuffle(-player.speed,0)
        elif(walk == "INV"):
            inventory()
        elif(walk == "LOOK"):
            look()
        elif(walk == "QUIT"):
            flag = False
        else:
            print("Command not recognized")

        if(player.hp<=0):
            print("You died. You got to level " + str(player.level) + " and had " + str(player.gold) + " Gold")
            flag = False
boot()
move()
