#import liberays
from random import seed
from random import randint

#player symbols
#first empty, player 1, player 2
psymbols= [" ", "o", "x"]

#move some function from main script to reduce clutter
#print out game screen 
def drawscreen(gamefield):
    print("  0 1 2")
    for ynum in range(len(gamefield)):
        lineoutput = str(ynum)
        for xnum in range(len(gamefield[ynum])):
            lineoutput = lineoutput + " " + selectplayersymbol(gamefield[ynum][xnum], psymbols)
        print(lineoutput)
        
#select the player symbol 
def selectplayersymbol(playernumber, playersymbols):
    return playersymbols[playernumber]

#select random player
def selectrandomplayer():
    seed()
    randomnum = randint(0, 100)
    if (randomnum > 50):
        return 1
    else:
        return 2
    
def getplayerinput(field):
    correctinput = False
    while not correctinput:
        plinx = input("please select x co-ord")
        pliny = input("please select y co-ord")
        try:
            if (int(plinx) > -1 and int(plinx) < 3):
                if (int(pliny) > -1 and int(pliny) < 3):
                    if (field[int(plinx)][int(pliny)] == 0):
                        correctinput = True
        except ValueError:
            print("A number has not been entered")
        if (correctinput == False):
            print("Incorect input please, select again")
    return [int(plinx), int(pliny)]