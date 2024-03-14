from microbit import display
from microbit import *
from visuals import *
import music

def startup():
    cup()
    music.pitch(622, 500)
    music.pitch(311, 125)
    music.pitch(466, 250)
    music.pitch(415, 500)
    music.pitch(622, 250)
    music.pitch(466, 250)
    sleep(1000)

def scrollAndReturnUsingAB(choices,question): # Input list of choices, scroll using buttons A and B, return value of choice
    maxNumChoices = len(choices) - 1 # Number of options in list starting at 0
    listChoice = 0
    currentChoice = ""
    
    while True:
        if pin_logo.is_touched(): # Press logo to select option
            music.pitch(500,duration=1,wait=False)
            music.pitch(500,duration=1)
            sleep(1000)
            return(choices[listChoice])

        if accelerometer.was_gesture('shake'): # Shake to show question again 
            music.pitch(500,duration=1) # Feedback beep
            display.scroll(question,80)

        if button_a.is_pressed(): # Go to previous option if button A pressed
            music.pitch(350,duration=1) # Feedback beep
            if listChoice == maxNumChoices:
                listChoice = 0
                currentChoice = choices[listChoice]
                display.scroll(choices[0],80)
                symbols(currentChoice)
            else:
                listChoice += 1
                display.scroll(choices[listChoice],80)
                currentChoice = choices[listChoice]
                symbols(currentChoice)

        if button_b.is_pressed(): # Go to next option if button B pressed
            music.pitch(650,duration=1) # Feedback beep
            if listChoice == 0:
                listChoice = maxNumChoices
                display.scroll(choices[maxNumChoices],80)
                currentChoice = choices[listChoice]
                symbols(currentChoice)
            else:
                listChoice -= 1
                display.scroll(choices[listChoice],80)
                currentChoice = choices[listChoice]
                symbols(currentChoice)
        

def feelingGNB(): # Returns if user is feeling "Good", "Bad", "Neutral"
    choicesGNB = ["Good","Neutral","Bad"]
    question = "hi. how are you?"
    
    # Shows question
    music.pitch(440,duration=1) # 
    display.scroll(question,80) # Scroll question
    
    leftRightArrow()
    userChoice = scrollAndReturnUsingAB(choicesGNB,question)
    return userChoice

def emotion1_10():
    num1_10 = ["1","2","3","4","5"]
    question = "How do you feel?"
    
    music.pitch(440,duration=1) # Feedback beep
    display.scroll(question,80) # Scroll question
    
    leftRightArrow()
    userChoice = scrollAndReturnUsingAB(num1_10,question)
    return userChoice

#def exportData(userEmotion,emotionIntensity,amountOfEmotions):
    #emotionNum = amountOfEmotions - 1
    #log.set_labels("Emotion","Intensity",timestamp=log.HOURS)
    #log.add({Emotion=userEmotion[emotionNum]
    #        Intensity=emotionIntensity[emotionNum]})

def export():
    while True:
        if pin_logo.is_touched():
            display.scroll("Log Data",100)
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
            
