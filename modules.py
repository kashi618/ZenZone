import microbit as mb

# Returns if user is feeling "good" or "bad"
def feelingGoodBad():
    mb.display.scroll("hi. how are you?",80)
    mb.display.scroll(choices[0])
    
    choices = ["Good","Bad"] # 0=Good  1=Bad
    currentChoice = 0
    
    while True:
        # When the logo is pressed, shows the message again
        if mb.pin_logo.is_touched():
            mb.display.scroll("hi. how are you?",80)
        
        # Cycle through options (good,bad) using button A and B
        if mb.button_a.is_pressed():
            if currentChoice == 0 :
                mb.display.scroll(choices[0],80)
                currentChoice += 1
            else:
                mb.display.scroll(choices[1],80)
                currentChoice -= 1
        if mb.button_b.is_pressed():
            if currentChoice == 0 :
                mb.display.scroll(choices[0],80)
                currentChoice += 1
            else:
                mb.display.scroll(choices[1],80)
                currentChoice -= 1
        
        # Returns the choice of the user as a string. ("good","bad")
        if mb.button_a.is_pressed() and mb.button_b.is_pressed():
            if currentChoice == 1:
                return "good"
            else:
                return "bad"
