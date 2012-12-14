from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
var speed = 5
while 1:

        sleep(speed * 0.1)
        GPIO.output(13, True)
        GPIO.output(15, False)
        sleep(speed * 0.1)
        GPIO.output(15, True)
        GPIO.output(16, False)
        sleep(speed * 0.1)
        GPIO.output(16, True)
                                
	if GPIO.input(11) && speed > 1:
		speed = speed - 1
	
	if GPIO.input(12) && speed < 10:
		speed = speed + 1
	
