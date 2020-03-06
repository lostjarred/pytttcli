#import liberays
from random import seed
from random import randint

#my libeary 
from gamefunctions import *

#array for gamefield
field = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]


    
startingplayer = selectrandomplayer()
print("The starting player is player " + str(startingplayer))

gamewon = False
curplayer = startingplayer
winingplayer = 0
while not gamewon :
    #inital draw the game field 
    drawscreen(field)
    
    #get player input, update field array 
    print("Player " +  str(curplayer) + " select a square")
    
    #get the playerinput
    playerinputs = getplayerinput(field)
    #seperate returned values into x and y
    playerinputy = playerinputs[1]
    playerinputx = playerinputs[0] 
                
                
    field[playerinputy][playerinputx] = curplayer
    
    #alternate the players
    if (curplayer == 1):
        curplayer = 2
    else:
        curplayer = 1
    #check for a winning player, if so trigger the end game
    winingplayer = checkforwin(field)
    
    if (winingplayer != 0):
        gamewon = True
        if (winingplayer > 0 ):
            print("the game has been won by player" + str(winingplayer))
        elif (winingplayer == -1):
            print("the game has run out of spaces, the game is a draw")

                            