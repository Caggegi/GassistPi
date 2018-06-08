#
#--------------Caggegi's Version--------------
#-----for my Elegoo touch screen 3.5 inch-----
#-----------Change button to GPIO20-----------

#!/usr/bin/env python
import time
import os
import os.path
import RPi.GPIO as GPIO
import subprocess
from actions import stop

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while GPIO.input(20):
    time.sleep(0.01)
    if not GPIO.input(20):
       print('Stopped')
       stop() 
