# Importing microbit dependencies and functions
from microbit import display
from microbit import *
from visuals import *
import music
import log

# Shows a cup image, and boot sound
def startup():
    cup()
    music.pitch(622, 500)
    music.pitch(311, 125)
    music.pitch(466, 250)
    music.pitch(415, 500)
    music.pitch(622, 250)
    music.pitch(466, 250)
    sleep(1000)

# By inputting a list of possible choices, the user can scroll through them using buttons A and B.
# Once a choice is picked by the user, the value is returned
def scrollAndReturnUsingAB(choices,question): 
    # Initializing variables
    maxNumChoices = len(choices) - 1 # Finds the total amount of choices
    listChoice = 0
    currentChoice = ""
    
    while True:
        if pin_logo.is_touched(): # Press logo to select option
            music.pitch(500,duration=1,wait=False)
            music.pitch(500,duration=1)
            sleep(1000)
            return(choices[listChoice])

        # Shake the microbit to show question again
        if accelerometer.was_gesture('shake'):
            music.pitch(500,duration=1) # Feedback beep
            display.scroll(question,80) # Scroll question again

        # Go to previous option if button A pressed
        if button_a.is_pressed(): 
            music.pitch(350,duration=1) # Feedback beep
            
            # When at the last choice, loop back to the start
            if listChoice == maxNumChoices: 
                listChoice = 0
                currentChoice = choices[listChoice]
                display.scroll(choices[0],80)
                symbols(currentChoice)
            # Go forward to the next choice
            else:
                listChoice += 1
                display.scroll(choices[listChoice],80)
                currentChoice = choices[listChoice]
                symbols(currentChoice)

        # Go to next option if button B pressed
        if button_b.is_pressed(): 
            music.pitch(650,duration=1) # Feedback beep
            
            # When at the first choice, loop back to the last choice
            if listChoice == 0: 
                listChoice = maxNumChoices
                display.scroll(choices[maxNumChoices],80)
                currentChoice = choices[listChoice]
                symbols(currentChoice)
            # Go backward to previous choice
            else:
                listChoice -= 1
                display.scroll(choices[listChoice],80)
                currentChoice = choices[listChoice]
                symbols(currentChoice)
        

def feelingGNB(): # Returns how the user feels. "Good", "Bad", "Neutral"
    choicesGNB = ["Good","Neutral","Bad"] # Values the user can input
    question = "hi. how are you?"         # Question for the user
    
    music.pitch(440,duration=1) # Feedback beep
    display.scroll(question,80) # Scrolls question for user
    leftRightArrow() # Arrow visual for button A and B
    
    # Uses scrollAndReturnUsingAB function to get user choice
    userChoice = scrollAndReturnUsingAB(choicesGNB,question)
    return userChoice # Returns the choice made by user

def emotion1_5(): # Returns how strong this emotion is felt. "1","2","3","4","5"
    num1_5 = ["1","2","3","4","5"] # Values the user can input
    question = "How do you feel?"  # Question for the user
    
    music.pitch(440,duration=1) # Feedback beep
    display.scroll(question,80) # Scrolls question for user
    leftRightArrow() # Arrow visual for button A and B
    
    # Uses scrollAndReturnUsingAB function to get user choice
    userChoice = scrollAndReturnUsingAB(num1_5,question)
    return userChoice # Returns the choice made by user

def exportData(emotion,intensity):
    while True:
        if pin_logo.is_touched():
            display.scroll("Log Data",100)
            
            # Adds data to csv file
            log.add(Emotion=emotion,Intensity=intensity)

            # Visual of arrow sending data from microbit to cable
            for i in range(3):
                upArrow()
            display.show(Image( "09090:"
                                "99999:"
                                "99999:"
                                "09990:"
                                "00900"))
            display.show(Image( "00000:"
                                "99099:"
                                "00000:"
                                "90009:"
                                "09990"))
            
