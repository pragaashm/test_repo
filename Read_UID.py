#/***********************************/
#/* Author:			Felix Knobl	    */
#/* Version:		1.0			    */
#/* Filename:		Read_UID.py     */
#/* Last modified:	25.11.2019	    */
#/*============================	    */
#/* Copyright (C) 2019			    */
#/***********************************/


import signal
import time
import MFRC522
import RPi.GPIO as GPIO

from _thread import start_new_thread

# Disable warnings for GPIOs
GPIO.setwarnings(False)

##########################
##      CardReader      ##
##########################

def StartCardReader():
    global UID_orig

    print("Function Call: StartCardReader()\n")

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    while True:

        # Scan for cards    
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        #print(TagType)
        # If a card is found
        if status != MIFAREReader.MI_OK:
            continue

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()
        
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            
            # Appends the four bytes together
            UID_orig = str(hex(uid[0])[2:].zfill(2)) + str(hex(uid[1])[2:].zfill(2)) + str(hex(uid[2])[2:].zfill(2)) + str(hex(uid[3])[2:].zfill(2))
            
            # Print the current date and time
            print("INFO: Card detected!")
            print("--------------------")
            print("Date: " + time.strftime("%a %d.%m.%Y"))
            print("Time: " + time.strftime("%H:%M:%S %Z"))
            print("UID:  " + UID_orig)
            print("\n") 


# Capture SIGINT for cleanup when the script is aborted
def ExitProgram(signal, frame):
    print ("Ctrl+C captured. Exiting program.")
    GPIO.cleanup()
    exit()

############
##  MAIN  ##
############

if __name__ == '__main__':
    print("Welcome to RFID Reader V1.0\nCopyright (C) 2019 Felix Knobl\nPress Ctrl+C to EXIT...\n")

    # Hook the SIGINT
    signal.signal(signal.SIGINT, ExitProgram)
    
    # Start the Card reader and the websocket 
    start_new_thread(StartCardReader, ())

   
