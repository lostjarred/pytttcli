#import liberays
import os
from random import seed
from random import randint

#player symbols
#first empty, player 1, player 2
psymbols= [" ", "o", "x"]

#clearscreen, solution by https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
#move some function from main script to reduce clutter
#print out game screen 
def drawscreen(gamefield):
    cls()
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

#get player input check if vaild either return value or ask for another     
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

#check for win conditions,return the player number, 0 if no winer, -1 if no winder + no moves remain
def checkforwin(field):
    #check for win conditions
    emptyspances = 0
    winingplayer = 0
    playercheck = 0
    
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
    if (emptyspances == 0 and winingplayer > 0):
        winingplayer = -1
    return winingplayer

#the main game function itself
def startgame():
    #array for gamefield
    field = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    #select the starting player
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
    #slight delay for message
    input("Press any key to continue")
