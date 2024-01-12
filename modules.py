import microbit as mb

def feelingGoodBad():
    mb.display.scroll("hi. how are you?",80)
    mb.display.scroll(choices[0])
    
    choices = ["Good","Bad"] # 0=Good  1=Bad
    currentChoice = 0
    
    while True:
        if mb.pin_logo.is_touched():
            mb.display.scroll("hi. how are you?",80)
        
        
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
        
        if mb.button_a.is_pressed() and mb.button_b.is_pressed():
            return currentChoice
