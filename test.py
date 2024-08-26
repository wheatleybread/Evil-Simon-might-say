import random
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


y = 3


list = []


piezo.freq(2000)
# piezo.duty_u16(1000)




while True:
    
    if redButton.value() == True:
        redLed.on()
    elif blueButton.value() == True:
        blueLed.on()
    elif greenButton.value() == True:
        greenLed.on()
    elif yellowButton.value() == True:
        print("bahh!!!!")
        yellowLed.on()
    sleep(0.2)
    

