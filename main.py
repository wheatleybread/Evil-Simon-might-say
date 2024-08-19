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

y = 3


list = []


piezo.freq(2000)
piezo.duty_u16(1000)


for x in range(y):
    list.append(random.randint(1,4))
    sleep(0.5)

print(list)
print(list[0])

while True:
    value = potometer.read_u16()
    potLed.on()
    print (f"Pot: {value}")
    if redButton.value() == True:
        redLed.on()
    elif blueButton.value() == True:
        blueLed.on()
    elif greenButton.value() == True:
        greenLed.on()
    elif yellowButton.value() == True:
        print("bahh!!!!)")
        yellowLed.on()
    sleep(0.2)
    

