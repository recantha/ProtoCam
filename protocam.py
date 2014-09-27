import os
import time
import RPi.GPIO as GPIO
import picamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN_BUTTON=25
GPIO.setup(PIN_BUTTON, GPIO.IN)
PIN_GREEN_LEFT=14
PIN_GREEN_RIGHT=15
PIN_YELLOW_LEFT=27
PIN_YELLOW_RIGHT=22
GPIO.setup(PIN_GREEN_LEFT, GPIO.OUT)
GPIO.setup(PIN_GREEN_RIGHT, GPIO.OUT)
GPIO.setup(PIN_YELLOW_LEFT, GPIO.OUT)
GPIO.setup(PIN_YELLOW_RIGHT, GPIO.OUT)

while True:
	if GPIO.input(PIN_BUTTON) == False:
		print "Button pressed"
		GPIO.output(PIN_GREEN_LEFT, 1)
		GPIO.output(PIN_GREEN_RIGHT, 1)
		GPIO.output(PIN_YELLOW_LEFT, 1)
		GPIO.output(PIN_YELLOW_RIGHT, 1)

		with picamera.PiCamera() as camera:
			camera.start_preview()
			camera.capture('/home/pi/image.jpg')
			camera.stop_preview()

	else:
		GPIO.output(PIN_GREEN_LEFT, 0)
		GPIO.output(PIN_GREEN_RIGHT, 0)
		GPIO.output(PIN_YELLOW_LEFT, 0)
		GPIO.output(PIN_YELLOW_RIGHT, 0)

	time.sleep(0.1)

