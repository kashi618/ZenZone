import microbit as mb
from microbit import display
import music

def startup():
    display.clear()
    for i in range (0,5):
        display.set_pixel(0,i,9)
        display.set_pixel(4,i,9)
    for i in range(1,4):
        display.set_pixel(i,1,5)
        display.set_pixel(i,2,5)
        display.set_pixel(i,3,5)
        display.set_pixel(i,4,9)
    
    music.pitch(622, 500)
    music.pitch(311, 125)
    music.pitch(466, 250)
    music.pitch(415, 500)
    music.pitch(622, 250)
    music.pitch(466, 250)
    
# Returns if user is feeling "good" or "bad"
def feelingGoodBad():
    choices = ["Good","Bad"] # 0=Good  1=Bad
    currentChoice = 0
    
    mb.display.scroll("hi. how are you?",80)
    
    while True:
        # When the logo is pressed, shows the message again
        if mb.pin_logo.is_touched():
            mb.display.scroll("hi. how are you?",80)
        
        # Cycle through options (good,bad) using button A and B
        if mb.button_a.is_pressed():
            if currentChoice == 0 :
                mb.display.scroll(choices[0],80)
                currentChoice += 1
            else:
                mb.display.scroll(choices[1],80)
                currentChoice -= 1
        if mb.button_b.is_pressed():
            if currentChoice == 0 :
                mb.display.scroll(choices[0],80)
                currentChoice += 1
            else:
                mb.display.scroll(choices[1],80)
                currentChoice -= 1
        
        # Returns the choice of the user as a string. ("good","bad")
        if mb.button_a.is_pressed() and mb.button_b.is_pressed():
            if currentChoice == 1:
                return "good"
            else:
                return "bad"