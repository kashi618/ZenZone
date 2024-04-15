from microbit import *
from modules import *
from visuals import *

# Initializing variables, and csv
amountOfEmotions = 0
log.set_labels("Emotion", "Intensity")

# Startup Picture 
startup()

# Grabs the emotion felt, and how strong they feel it from user.
# This data would be gathered every hour, and then stored on a csv file on the microbit
while True:
    amountOfEmotions += 1
    
    # feelingGNB() is used for gathering the emotion felt
    # emotion1_5 is used for gathering how strong they feel this way
    exportData(feelingGNB(),emotion1_5())
    
    sleep(3600000) # 1 hour timer