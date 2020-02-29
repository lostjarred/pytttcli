#import liberays
from random import seed
from random import randint

#array for gamefield
field = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#player symbols
#first empty, player 1, player 2
psymbols= [" ", "o", "x"]

#print out game screen 
def drawscreen():
    print(" 0 1 2")
    print("0", field[0][0], field[0][1], field[0][2])
    print("1", field[1][0], field[1][1], field[1][2])
    print("2", field[2][0], field[2][1], field[2][2])
    
#select random player
def selectrandomplayer():
    seed()
    randomnum = randint(0, 100)
    if (randomnum > 50):
        return 1
    else:
        return 2
    
startingplayer = selectrandomplayer()
print("The starting player is player " + str(startingplayer))

gamewon = False
curplayer = startingplayer
winingplayer = 0
while not gamewon :
    #inital draw the game field 
    drawscreen()
    
    #get player input, update field array 
    print("Player " +  str(curplayer) + "select a square")
    
    #test input
    correctinput = False
    while not correctinput:
        plinx = input("please select x co-ord")
        pliny = input("please select y co-ord")
        try:
            if (int(plinx) > -1 and int(plinx) < 3):
                if (int(pliny) > -1 and int(pliny) < 3):
                    correctinput = True
        except ValueError:
            print("A number has not been entered")
        if (correctinput == False):
            print("Incorect input please, select again")
                
                
    field[int(plinx)][int(pliny)] = curplayer
    
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

                            