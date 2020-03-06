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