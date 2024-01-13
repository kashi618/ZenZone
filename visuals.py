from microbit import display
from microbit import *

def cup(): # Water Cup
    display.show(Image( "90009:"
                        "95559:"
                        "95659:"
                        "96669:" 
                        "99999"))

def symbolGNB(x): # Symbols for Good, Neutral, Bad
    if x == 0: # Good
        display.show(Image( "99999:"
                            "90000:"
                            "90999:"
                            "90009:" 
                            "99999"))
    
    if x == 1: # Neutral
        display.show(Image( "90009:"
                            "99009:"
                            "90909:"
                            "90099:" 
                            "90009"))
    
    if x == 2: # bad
        display.show(Image( "99990:"
                            "99009:"
                            "99990:"
                            "90009:" 
                            "99990"))
