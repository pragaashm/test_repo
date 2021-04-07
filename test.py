import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep


GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)


reader = SimpleMFRC522()

while True:
        try:

            id, text = reader.read()
            print(id)
            print(type(id))
            "print(text)"
            sleep(1)

            if id==473653218634:
                sleep(1)
                print('Hei Pragaash Mohan')
                print('Du er kul')
                print('Ta en pullup')
                sleep(1)

            else:
                print('Hvem er du?')
                sleep(1)
                print('Prøv igjen')
        except:
                GPIO.cleanup()
