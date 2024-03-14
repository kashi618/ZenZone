from microbit import display
from microbit import *

def cup(): # Water Cup
    display.show(Image( "90009:"
                        "95559:"
                        "95659:"
                        "96669:" 
                        "99999"))

def leftRightArrow():
    display.show(Image( "00000:"
                        "09090:"
                        "99099:"
                        "09090:" 
                        "00000"))
    

def upArrow(): # Water Cup
    display.show(Image( "00900:"
                        "09990:"
                        "90909:"
                        "00900:" 
                        "00900"))
    sleep(100)
    display.show(Image( "09990:"
                        "90909:"
                        "00900:"
                        "00900:"
                        "00000"))
    sleep(100)
    display.show(Image( "90909:"
                        "00900:"
                        "00900:"
                        "00000:"
                        "00000"))
    sleep(100)
    display.show(Image( "00900:"
                        "00900:"
                        "00000:"
                        "00000:"
                        "00000"))
    sleep(100)
    display.show(Image( "00900:"
                        "00000:"
                        "00000:"
                        "00000:"
                        "00000"))
    sleep(100)
    display.show(Image( "00000:"
                        "00000:"
                        "00000:"
                        "00000:"
                        "00000"))
    sleep(100)
    display.show(Image( "00000:"
                        "00000:"
                        "00000:"
                        "00000:"
                        "00900"))
    sleep(100)
    display.show(Image( "00000:"
                        "00000:"
                        "00000:"
                        "00900:"
                        "09990"))
    sleep(100)
    display.show(Image( "00000:"
                        "00000:"
                        "00900:"
                        "09990:"
                        "90909"))
    sleep(100)
    display.show(Image( "00000:"
                        "00900:"
                        "09990:"
                        "90909:"
                        "00900"))
    sleep(100)


def symbols(x): # Symbols for Good, Neutral, Bad
    if x == "Good": # Good
        display.show("G")
    
    if x == "Neutral": # Neutral
        display.show("N")
    
    if x == "Bad": # bad
        display.show("B")
    
    if x == "1":
        display.show("1")
        
    if x == "2":
        display.show("2")
        
    if x == "3":
        display.show("3")
        
    if x == "4":
        display.show("4")
    
    if x == "5":
        display.show("5")
        