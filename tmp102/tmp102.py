#!/usr/bin/python

import smbus
import time
import datetime

bus = smbus.SMBus(1)

data = bus.read_i2c_block_data(0x48, 0)
msb = data[0]
lsb = data[1]
# Print degrees Celsius
out = (((msb << 8) | lsb) >> 4) * 0.0625
print "%f|%s"%( out, datetime.datetime.now()) 
