from microbit import display
from microbit import *
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

def scrollAndReturnUsingAB(choices,question): # Input list of choices, scroll using buttons A and B, return value of choice
    maxNumChoices = len(choices) - 1 # Number of options in list starting at 0
    currentChoice = 0
    
    while True:
        if pin_logo.is_touched(): # Show question again on logo touch
            music.pitch(500,duration=1) # Beep for feedback
            display.scroll(question,80)

        if accelerometer.was_gesture('2g'): # Shake microbit to select current option
            sleep(1000)
            return(choices[currentChoice])

        if button_a.is_pressed(): # Go to previous option if button A pressed
            music.pitch(440,duration=1) # Beep for feedback
            if currentChoice == maxNumChoices:
                currentChoice = 0
                display.scroll(choices[0],80)
                symbolGNB(currentChoice)
            else:
                currentChoice += 1
                display.scroll(choices[currentChoice],80)
                symbolGNB(currentChoice)

        if button_b.is_pressed(): # Go to next option if button B pressed
            music.pitch(440,duration=1) # Beep for feedback
            if currentChoice == 0:
                currentChoice = maxNumChoices
                display.scroll(choices[maxNumChoices],80)
                symbolGNB(currentChoice)
            else:
                currentChoice -= 1
                display.scroll(choices[currentChoice],80)
                symbolGNB(currentChoice)
        

def feelingGNB(): # Returns if user is feeling "Good", "Bad", "Neutral"
    choicesGNB = ["Good","Neutral","Bad"]
    question = "hi. how are you?"
    
    # Shows question
    music.pitch(440,duration=1) # Beep for feedback
    display.scroll(question,80)
    
    userChoice = scrollAndReturnUsingAB(choicesGNB,question)
    return userChoice

def emotion1_10():
    num1_10 = ["1","2","3","4","5"]
    question = "How do you feel?"
    
    music.pitch(440,duration=1) # Beep for feedbackw
    display.scroll(question,80) 
    
    userChoice = scrollAndReturnUsingAB(num1_10,question)
    return userChoice
