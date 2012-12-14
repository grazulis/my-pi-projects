from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
speed = 5

def checkbutton():                                
	if GPIO.input(11) and speed > 1:
		speed = speed - 1	
	if GPIO.input(12) and speed < 10:
		speed = speed + 1
		
while 1:
	checkbutton()
        sleep(speed * 0.1)
        GPIO.output(13, True)
        GPIO.output(16, False)
        checkbutton()
	sleep(speed * 0.1)
        GPIO.output(16, True)
        GPIO.output(15, False)
        checkbutton()
	sleep(speed * 0.1)
        GPIO.output(15, True)
	GPIO.output(13, False)


	
