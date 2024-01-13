from microbit import display
import music
from visuals import*

def startup():
    cup()
    music.pitch(622, 500)
    music.pitch(311, 125)
    music.pitch(466, 250)
    music.pitch(415, 500)
    music.pitch(622, 250)
    music.pitch(466, 250)

# Returns if user is feeling "Good" or "Bad"
def feelingGNB():
    # List for choices
    choices = ["Good","Neutral","Bad"] # 0=Good 1=Neutral 2=Bad
    currentChoice = 0
    
    display.scroll("hi. how are you?",80)
    
    while True:
        # When the logo is pressed, shows the message again
        if pin_logo.is_touched():
            display.scroll("hi. how are you?",80)
        
        # Cycle through options (Good,Neutral,Bad) using buttons A and B
        if button_a.is_pressed(): # Button A
            if currentChoice == 0:
                currentChoice = 2
                display.scroll(choices[currentChoice],80)
                symbolGNB(currentChoice)
            else:
                currentChoice -= 1
                display.scroll(choices[currentChoice],80)
                symbolGNB(currentChoice) 
        if button_b.is_pressed(): # Button B
            if currentChoice == 2:
                currentChoice = 0
                display.scroll(choices[currentChoice],80)
                symbolGNB(currentChoice)
            else: 
                currentChoice += 1
                display.scroll(choices[currentChoice],80)
                symbolGNB(currentChoice)
        
        # Returns the choice of the user as a string. "good","bad"
        if button_a.is_pressed() and button_b.is_pressed():
            return str(choices[currentChoice])
