from microbit import display
from microbit import *

def cup(): # Water Cup
    display.show(Image( "90009:"
                        "95559:"
                        "95659:"
                        "96669:" 
                        "99999"))

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
        