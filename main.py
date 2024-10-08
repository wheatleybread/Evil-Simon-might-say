from random import randint
from time import sleep
from machine import Pin, PWM, ADC
from piezoNotes import *


# Defining buttons
redButton = Pin(2, Pin.IN)
blueButton = Pin(0, Pin.IN)
greenButton = Pin(3, Pin.IN)
yellowButton = Pin(1, Pin.IN)

#Defining Piezo
piezo = PWM(Pin(20))

#Defining lights
redLed = Pin(14, Pin.OUT)
blueLed = Pin(12, Pin.OUT)
greenLed = Pin(15, Pin.OUT)
yellowLed = Pin(13, Pin.OUT)


#Setting up the iezo
def PlayNote(note, duration):
    piezo.freq(notes[note])
    piezo.duty_u16(1000)
    sleep(duration)
    piezo.duty_u16(0)


#Basic variables
length = 0
choice = 0
playerlist = []
gamelist = []
level = 1
list = 0

#The game
def game():
    global length, level, gamelist, playerlist, list, choice, x

    #randomising buttons
    while True:
        for x in range(1):
            gamelist.append(randint(1,4))
        for x in range(level):
            playerturn = False
            sleep(0.5)
            print(list)
            choice = gamelist[list]
            if choice == 1:
                redLed.on()
                PlayNote("C5", 0.4)
                redLed.off()
                list += 1
            elif choice == 2:
                blueLed.on()
                PlayNote("C3", 0.4)
                blueLed.off()
                list += 1
            elif choice == 3:
                greenLed.on()
                PlayNote("C6", 0.4)
                greenLed.off()
                list += 1
            elif choice == 4:
                yellowLed.on()
                PlayNote("C4", 0.4)
                yellowLed.off()
                list += 1
            playerturn = True


        #taking player input
        for x in range(level):      
            while playerturn == True:
                if redButton.value() == True:
                    playerlist.append(1)
                    sleep(0.1)
                    playerturn = False
                elif blueButton.value() == True:
                    playerlist.append(2)
                    sleep(0.1)
                    playerturn = False
                elif greenButton.value() == True:
                    playerlist.append(3)
                    sleep(0.1)
                    playerturn = False
                elif yellowButton.value() == True:
                    playerlist.append(4)
                    sleep(0.1)
                    playerturn = False
            #if correct
            if playerlist[length] == gamelist[length]:
                    print('Yay!')
                    PlayNote("E5", 0.25)
            #if incorrect
            else:
                print ("Lost!")
                PlayNote("B0", 0.5)
                redLed.on()
                blueLed.on()
                greenLed.on()
                yellowLed.on()
                sleep(1)
                redLed.off()
                greenLed.off()
                yellowLed.off()
                blueLed.off()
                print("DIE")
                gamelist = []
                level = 0
                break
            length += 1
            playerturn = True
        level += 1
        length = 0
        list = 0
        playerlist = []



game()