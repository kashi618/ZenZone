import microbit as mb

def cup():
    for i in range (0,5):
        mb.display.set_pixel(0,i,9)
        mb.display.set_pixel(4,i,9)
    for i in range(1,4):
        mb.display.set_pixel(i,1,3)
        mb.display.set_pixel(i,2,3)
        mb.display.set_pixel(i,3,3)
        mb.display.set_pixel(i,4,9)

