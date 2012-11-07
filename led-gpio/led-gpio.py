from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
while 1:
	if GPIO.input(11):
		GPIO.output(13, False)
		sleep(0.2)
		GPIO.output(13, True)
		GPIO.output(15, False)
		sleep(0.2)
		GPIO.output(15, True)
		GPIO.output(16, False)
		sleep(0.2)
		GPIO.output(16, True)
	else:
		GPIO.output(13, True)
		GPIO.output(15, True)
		GPIO.output(16, True)

	if GPIO.input(12):
		GPIO.output(15, False)
	else:
		GPIO.output(15, True)
