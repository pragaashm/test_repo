import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep


GPIO.setwarnings(False)    


reader = SimpleMFRC522()

rfid_Y = True;

while rfid_Y:
        try:

            id, text = reader.read()
            print(id)
            print(type(id))
            "print(text)"
            sleep(1)

            if id==904913957185:
                sleep(1)
                print('Hei Pragaash Mohan')
                sleep(1)
                print('Du er kul')
                sleep(1)
                print('Ta en pullup')
                sleep(1)
            
            elif id == 926582318801:
                sleep(1)
                print('Hei Andreas Glomsrud')
                sleep(1)
                print('Last ned Tinder')
                sleep(1)

            else:
                print('Hvem er du?')
                sleep(1)
                print('Prøv igjen')
        except:
                GPIO.cleanup()
