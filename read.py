import RPi.GPIO as GPIO
import keyboard

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


            keyboard.send(str(id))
            sleep(1)

            print(keyboard.send(str(id)))
            print(type(keyboard.send(str(id))))
            sleep(1)

        except:
                GPIO.cleanup()