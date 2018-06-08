#
#--------------Caggegi's Version--------------
#-----for my Elegoo touch screen 3.5 inch-----
#-----------Change button to GPIO16-----------

#!/usr/bin/env python
import time
import os
import os.path
import RPi.GPIO as GPIO
import subprocess
from actions import stop

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while GPIO.input(20):
    time.sleep(0.01)
    if not GPIO.input(16):
       print('Stopped')
       stop() 
