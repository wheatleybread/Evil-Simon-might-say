import random
from time import sleep
from machine import Pin, PWM, ADC

redButton = Pin(17, Pin.IN)
blueButton = Pin(19, Pin.IN)
greenButton = Pin(20, Pin.IN)
yellowButton = Pin(18, Pin.IN)
piezo = PWM(Pin(14))
potometer = ADC(Pin(26))
redLed = Pin(11, Pin.OUT)
blueLed = Pin(9, Pin.OUT)
greenLed = Pin(10, Pin.OUT)
yellowLed = Pin(12, Pin.OUT)
potLed = Pin(8, Pin. OUT)

gamelist = []
playerlist = []
level = 0

while True:
    gamelist.append(random.randint(1,5))
    sleep(0.5)
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
        else:
            yellowLed.on()
            
    

