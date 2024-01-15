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

def scrollAndReturnUsingAB(choices,question): # Input list of choices, scroll using buttons A and B, return value of choice
    maxNumChoices = len(choices) - 1 # Number of options in list starting at 0
    currentChoice = 0
    
    while True:
        # When the logo is pressed, shows the question again
        if pin_logo.is_touched():
            display.scroll(question,80)
        
        if button_a.is_pressed(): # Go to next option when button A is pressed
            if currentChoice == maxNumChoices:
                currentChoice = 0
                display.scroll(choices[0],80)
                symbolGNB(currentChoice)
            else:
                currentChoice += 1
                display.scroll(choices[currentChoice],80)
                symbolGNB(currentChoice)
        
        if button_b.is_pressed():
            return choices[currentChoice]
    
    # [UNUSED]  scroll using button B
    # elif button_b.is_pressed(): # Button B
    #   if currentChoice == numChoices:
    #        currentChoice = 0
    #        display.scroll(choices[currentChoice],80)
    #        symbolGNB(currentChoice)
    #    else: 
    #        currentChoice += 1
    #        display.scroll(choices[currentChoice],80)
    #        symbolGNB(currentChoice)

def feelingGNB(): # Returns if user is feeling "Good", "Bad", "Neutral"
    choicesGNB = ["Good","Neutral","Bad"]
    question = "hi. how are you?"
    # Shows question
    display.scroll(question,80)
    
    return scrollAndReturnUsingAB(choicesGNB,question)

def feelingGood():
    display.scroll("Thats good!!")
    # add happy victory sfx

def feelingNeutral():
    display.scroll("")
    # neutral sfx

def feelingBad():
    display.scroll("Thats not good :(")
    # add sad sfx

