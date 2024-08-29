from random import randint
from time import sleep
from machine import Pin, PWM, ADC
from piezoNotes import *

class Homer:

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

    #Basic variables
    length = 0
    choice = 0
    playerlist = []
    gamelist = []
    level = 1
    list = 0

    #Setting up the iezo
    def PlayNote(self, note, duration):
        self.piezo.freq(notes[note])
        self.piezo.duty_u16(1000)
        sleep(duration)
        self.piezo.duty_u16(0)



    def sequencedisplay(self):
        for x in range(self.level):
                self.playerturn = False
                sleep(0.5)
                print(self.list)
                choice = self.gamelist[self.list]
                if choice == 1:
                    self.redLed.on()
                    self.PlayNote("C5", 0.4)
                    self.redLed.off()
                    self.list += 1
                elif choice == 2:
                    self.blueLed.on()
                    self.PlayNote("C3", 0.4)
                    self.blueLed.off()
                    self.list += 1
                elif choice == 3:
                    self.greenLed.on()
                    self.PlayNote("C6", 0.4)
                    self.greenLed.off()
                    self.list += 1
                elif choice == 4:
                    self.yellowLed.on()
                    self.PlayNote("C4", 0.4)
                    self.yellowLed.off()
                    self.list += 1
                self.playerturn = True


    def playertime(self):
        for x in range(self.level):      
                while self.playerturn == True:
                    if self.redButton.value() == True:
                        self.playerlist.append(1)
                        sleep(0.1)
                        self.playerturn = False
                    elif self.blueButton.value() == True:
                        self.playerlist.append(2)
                        sleep(0.1)
                        self.playerturn = False
                    elif self.greenButton.value() == True:
                        self.playerlist.append(3)
                        sleep(0.1)
                        self.playerturn = False
                    elif self.yellowButton.value() == True:
                        self.playerlist.append(4)
                        sleep(0.1)
                        self.playerturn = False
                #if correct
                if self.playerlist[self.length] == self.gamelist[self.length]:
                        print('Yay!')
                        self.PlayNote("E5", 0.25)
                #if incorrect
                else:
                    print ("Lost!")
                    self.PlayNote("B0", 0.5)
                    self.redLed.on()
                    self.blueLed.on()
                    self.greenLed.on()
                    self.yellowLed.on()
                    sleep(1)
                    self.redLed.off()
                    self.greenLed.off()
                    self.yellowLed.off()
                    self.blueLed.off()
                    print("DIE")
                    self.gamelist = []
                    self.level = 0
                    break
                self.length += 1
                self.playerturn = True

    #The game
    def game(self):

        #randomising buttons
        while True:
            for x in range(1):
            #adding random value to list
                self.gamelist.append(randint(1,4))
            #displaying input
            self.sequencedisplay()

            #taking player input
            self.playertime()
            #adding to level and resetting values
            self.level += 1
            self.length = 0
            self.list = 0
            self.playerlist = []

Bart = Homer()


Bart.game()