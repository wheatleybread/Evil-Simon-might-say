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

