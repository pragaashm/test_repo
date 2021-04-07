import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep


GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, GPIO.LOW)
reader = SimpleMFRC522()
while True:
        try:

            id, text = reader.read()
            print(id)
            print(type(id))
            print(text)
            sleep(2)

            if id==473652318634:
                print('Hei Pragaash Mohan')
                print('Du er kul')
                print('Ta en pullup')

            else:
        except:
                GPIO.cleanup()
