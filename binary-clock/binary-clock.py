# Python script for a binay clock display
# Control via an MCP23017 I2C IO Expander
# Code based on LED Chaser project form SK Pang Electronics
# GNU GPL V3

# Written by G. D. Leeming, Dec. 2012


import smbus
import sys
import getopt
import time 
bus = smbus.SMBus(0)

address = 0x20 # I2C address of MCP23017
bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 



def set_led(data,bank):
  if bank == 1:
   bus.write_byte_data(address,0x12,data)
  else:
   bus.write_byte_data(address,0x13,data)
  return


