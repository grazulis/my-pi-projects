# Python script for a binay clock display
# Control via an MCP23017 I2C IO Expander
# Code based on LED Chaser project form SK Pang Electronics
# GNU GPL V3

# Written by G. D. Leeming, Dec. 2012


#import smbus
#import sys
#import getopt
import time
from time import strftime
 
#bus = smbus.SMBus(0)

#address = 0x20 # I2C address of MCP23017
#bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
#bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 

#def set_led(data,value,bank):
#  if bank == 1:
#   bus.write_byte_data(address,0x12,data)
#  else:
#   bus.write_byte_data(address,0x13,data)
#  return

displayArray = [13]
oldTime = "0000"

def setTime(currentTime):
	x = 0
	checkArray = [2, 4, 3, 4] # This provides the structure for the LED format for HHMM
	timeArray = []
	
	# Need to check if this is needed for, e.g. 0950 (9:50 in the morning)
	#if len(currentTime) < 4:
	#	currentTime = "0" + currentTime 

	while x < 4:
		binaryValue = str(bin(int(currentTime[x:x+1])))[2:]
		while len(binaryValue) < checkArray[x]:
			binaryValue = "0" + binaryValue
		timeArray.append(binaryValue)				
		x=x+1
	print currentTime
	print timeArray

	displayArray = list(''.join(timeArray))
	print displayArray

	return 

def main():
	global oldTime		
	global displayArray
	while 1:
		
		currentTime = strftime("%H%M")
		if currentTime != oldTime:
			setTime(currentTime)
			for x in range(0,5):
				a = 1 << x 
#				set_led(a,displayArray[x], 0)
			for x in range(6,12):
				a = 1 << x
#				set_led(a, displayArray[x], 1)
			oldTime = currentTime

if __name__ == "__main__":
	main()

