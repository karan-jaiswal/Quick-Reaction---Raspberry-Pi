from gpiozero import LED, Button
from time import sleep
from random import uniform

left_name = input('left player name is ')
right_name = input('right player name is ')

led = LED(4)
right_button = Button(15)
left_button = Button(14)

led.on()
sleep(uniform(5, 10))
led.off()

#def pressed(button):
#	print(str(button.pin.number) + ' won the game')

def pressed(button):
    if button.pin.number == 14:
        print(left_name + ' won the game')
    else:
        print(right_name + ' won the game')
    exit()


right_button.when_pressed = pressed(right_button)
left_button.when_pressed = pressed(left_button)