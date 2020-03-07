#import liberays
from random import seed
from random import randint

#my libeary 
from gamefunctions import *
quit=False

while (quit == False):
    startgame()
    userinput = input("Would you like to quit Y/N")
    if (userinput == "y" or userinput == "Y"):
        quit = True
    elif (userinput == "n" or userinput == "N"):
        startgame()
    else:
        print("Invaild input, plese answer again") 
    
    
                            