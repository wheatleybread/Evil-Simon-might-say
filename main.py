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
level = 3
list = 0

while True:
    
    for x in range(level):
        gamelist.append(randint(1,4))
        sleep(0.5)
        choice = gamelist[list]
        if choice == 1:
            redLed.on()
            sleep(0.5)
            redLed.off()
            list += 1
        elif choice == 2:
            blueLed.on()
            sleep(0.5)
            blueLed.off()
            list += 1
        elif choice == 3:
            greenLed.on()
            sleep(0.5)
            greenLed.off()
            list += 1
        elif choice == 4:
            yellowLed.on()
            sleep(0.5)
            yellowLed.off()
            list += 1
    break   

for x in range(level):
    if redButton.value == True:
        playerlist.append(1)
        sleep(0.5)
    elif blueButton.value == True:
        playerlist.append(2)
        sleep(0.5)
    elif greenButton.value == True:
        playerlist.append(3)
        sleep(0.5)
    elif yellowButton.value == True:
        playerlist.append(4)
        sleep(0.5)

if playerlist == gamelist:
    print('Yay!')