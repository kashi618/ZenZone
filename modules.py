import microbit as mb

def welcomeMSG():
    mb.display.scroll("hi. how are you?",80)
    
    while True:
        if mb.pin_logo.is_touched():
            mb.display.scroll("hi. how are you?",80)
        
        if (mb.button_a.is_pressed()) and (mb.button_b.is_pressed()):
            mb.display.scroll("hi, how are you?",100)