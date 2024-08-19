import random
from time import sleep
from machine import Pin, PWM, ADC

redButton = Pin(17, Pin.IN)
blueButton = Pin(19, Pin.IN)
greenButton = Pin(20, Pin.IN)
yellowButton = Pin(18, Pin.IN)
piezo = PWM(Pin(14))
potometer = ADC(Pin(26))
redLed = Pin(11)
blueLed = Pin(9)
greenLed = Pin(10)
yellowLed = Pin(12)

y = 3


list = []


for x in range(y):
    list.append(random.randint(1,4))
    sleep(0.5)

while True:
    redButton.on()
    blueButton.on()
    greenButton.on()
    yellowButton.on()
    

