from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
speed = 5

def checkbutton(speed):                                
	if GPIO.input(11) and speed > 1:
		speed = speed - 1	
	if GPIO.input(12) and speed < 10:
		speed = speed + 1
		
while 1:
        pins = [13, 16, 15]
        
        for pin in pins:
                checkbutton(speed)
                GPIO.output(pin, False)
                sleep(speed * 0.1)
                GPIO.output(pin, True)
        

	
