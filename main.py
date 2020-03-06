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
    #check for win conditions
    emptyspances = 0
    for xfield in range(2):
        for yfield in range(2):
            if (field[xfield][yfield] > 0):
                playercheck = field[xfield][yfield]
                
                #check the up
                if (yfield > 0 and yfield < 2):
                    if (field[xfield][yfield - 1] == playercheck):
                        if (field[xfield][yfield] == playercheck):
                            if (field[xfield][yfield + 1] == playercheck):
                                winingplayer = playercheck
                #check the sides
                if (xfield > 0 and xfield < 2):
                    if (field[xfield - 1][yfield] == playercheck):
                        if (field[xfield][yfield] == playercheck):
                            if (field[xfield + 1][yfield] == playercheck):
                                winingplayer = playercheck
                                
                if (xfield == 0 and yfield == 0):
                    #check dianague 1
                    if (field[xfield - 1][yfield - 1] == playercheck):
                        if (field[xfield][yfield] == playercheck):
                            if (field[xfield + 1][yfield + 1] == playercheck):
                                winingplayer = playercheck
                    #check dianague 2
                    if (field[xfield + 1][yfield - 1] == playercheck):
                        if (field[xfield][yfield] == playercheck):
                            if (field[xfield + - 1][yfield + 1] == playercheck):
                                winingplayer = playercheck
            elif(field[xfield][yfield] == 0):
                emptyspances = emptyspances + 1
    #check for a winning player, if so trigger the end game
    if (winingplayer > 0):
        gamewon = True
    elif (emptyspances == 0):
        gamewon = True
        winingplayer = -1
    
if (gamewon):
    if (winingplayer > 0 ):
        print("the game has been won by player" + str(winingplayer))
    elif (winingplayer == -1):
        print("the game has run out of spaces, the game is a draw")

                            