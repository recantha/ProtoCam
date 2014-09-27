import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN_BUTTON=25
GPIO.setup(PIN_BUTTON, GPIO.IN)

while True:
	if GPIO.input(PIN_BUTTON) == False:
		print "Button pressed"
		print GPIO.input(PIN_BUTTON)
		time.sleep(1)

	else:
		os.system('clear')
		print "Waiting for you to press the button"

	time.sleep(0.5)

