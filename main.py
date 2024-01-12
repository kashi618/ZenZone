import microbit as mb
from microbit import *
from modules import *
from visuals import *

# DOCUMENTATION
# https://microbit-micropython.readthedocs.io/en/v2-docs/
# MICROBIT WEBSITE
# https://makecode.microbit.org/v3.1

# 0=Good  1=Bad
userChoice = welcomeMSG()

if userChoice == "good":
    