# Python script for a binay clock display Control via an MCP23017 I2C IO Expander Code based on LED Chaser 
# project form SK Pang Electronics GNU GPL V3

# Written by G. D. Leeming, Dec. 2012


import smbus
import sys
import getopt
import time
from time import strftime
 
bus = smbus.SMBus(1)

address = 0x20 # I2C address of MCP23017
bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 
displayArray = []
oldTime = "0000"

def set_led(data,bank):
  if bank == 1:
   bus.write_byte_data(address,0x12,data)
  else:
   bus.write_byte_data(address,0x13,data)
  return


def setTime(currentTime):
	global displayArray
        #Returns array of binary values representing the time as hh,mm
	displayArray = []
	x = 0
	checkArray = [2, 4, 3, 4] # This provides the structure for the LED format for HHMM

	timeString = ""
	currentTime = currentTime 

	while x < 4:
		binaryValue = str(bin(int(currentTime[x:x+1])))[2:]
		while len(binaryValue) < checkArray[x]:
                        print binaryValue
			binaryValue = "0" + binaryValue				
                timeString = timeString + binaryValue
		x=x+1
	print currentTime
	print timeString
        
	#TODO Change so uses integers?
	displayArray.append( list(timeString)[:6] )
	displayArray.append( list(timeString)[6:] )
	print displayArray

	return 

def main():
	global oldTime		
	#global displayArray
	while 1:
		
		currentTime = strftime("%H%M")
		if currentTime != oldTime:
			setTime(currentTime)
			banka = 0
			bankb = 0
			for x in range(0,6):
				if displayArray[0][x] == "1":
					a = 1 << x 
					banka = banka + a	
			print banka
			set_led(banka, 0)
			for x in range(0,7):
				if displayArray[1][x] == "1":
					a = 1 << x
					bankb = bankb + a
			print bankb	
			set_led(bankb, 1)
			oldTime = currentTime

if __name__ == "__main__":
	main()

