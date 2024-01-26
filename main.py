from microbit import *
from modules import *
from visuals import *

# DOCUMENTATION
# https://microbit-micropython.readthedocs.io/en/v2-docs/
# MICROBIT WEBSITE
# https://makecode.microbit.org/

# Startup Picture
startup()

while True:
    # (Good,Neutral,Bad)
    userEmotion = feelingGNB()
    rank = emotion1_10()
    
    sleep(3600000) # Wait for 1 hour