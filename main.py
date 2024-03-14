from microbit import *
from modules import *
from visuals import *

# DOCUMENTATION
# https://microbit-micropython.readthedocs.io/en/v2-docs/
# MICROBIT WEBSITE
# https://makecode.microbit.org/

# Startup Picture 
startup()

amountOfEmotions = 0

while True:
    
    userEmotion = feelingGNB()
    emotionIntensity = emotion1_10()
    #amountOfEmotions += 1
    #exportData(userEmotion,emotionIntensity,amountOfEmotions)
    export()
    
    
    sleep(3600000) # Wait for 1 hour
    