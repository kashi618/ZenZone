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
        
        if button_a.is_pressed() and button_b.is_pressed():
            return choices[currentChoice]
        
        elif button_a.is_pressed(): # Go to next option when button A is pressed
            
            music.pitch(440,duration=1)
            
            if currentChoice == maxNumChoices:
                currentChoice = 0
                display.scroll(choices[0],80)
                symbolGNB(currentChoice)
            else:
                currentChoice += 1
                display.scroll(choices[currentChoice],80)
                symbolGNB(currentChoice)
        
        elif button_b.is_pressed(): # Go to next option when button A is pressed
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
    display.scroll(question,80)
    
    return scrollAndReturnUsingAB(choicesGNB,question)

def emotion1_10():
    num1_10 = ["1","2","3","4","5"]
    question = "How do you feel?"
    display.scroll(question,80)
    
    return scrollAndReturnUsingAB(num1_10,question)
    
