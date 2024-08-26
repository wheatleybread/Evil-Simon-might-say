from random import randint
from time import sleep
from machine import Pin, PWM, ADC

redButton = Pin(2, Pin.IN)
blueButton = Pin(0, Pin.IN)
greenButton = Pin(3, Pin.IN)
yellowButton = Pin(1, Pin.IN)
piezo = PWM(Pin(20))

redLed = Pin(14, Pin.OUT)
blueLed = Pin(12, Pin.OUT)
greenLed = Pin(15, Pin.OUT)
yellowLed = Pin(13, Pin.OUT)




choice = 0
gamelist = []
playerlist = []
level = 1

while True:
    gamelist.append(randint(1,5))
    for x in range(level):
        choice = gamelist[level]
        if choice == 1:
            redLed.on()
            sleep(0.5)
            redLed.off()
        elif choice == 2:
            blueLed.on()
            sleep(0.5)
            blueLed.off()
        elif choice == 3:
            greenLed.on()
            sleep(0.5)
            greenLed.off()
        elif choice == 4:
            yellowLed.on()
            sleep(0.5)
            yellowLed.off()
       
    break

    

