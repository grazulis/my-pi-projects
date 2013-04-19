from espeak import espeak
from datetime import datetime
import time
import os

espeak.synth("Starting")
time.sleep(0.5)
os.system('clear') 

# Prefix might be needed to cope with some isues with delay over HDMI
t = "hello world"
prefix = "%s " %t

message1 = ["What is your name?", "Hello "]
message2 = ["How old are you?", " you are "]

espeak.synth(prefix + message1[0])
print message1[0],
reply1 = raw_input()
time.sleep(2)

espeak.synth(prefix + message2[0])
print message2[0],
reply2 = raw_input()
time.sleep(2)

print "%s %s, %s %s " %(message1[1], reply1, message2[1], reply2)

checkThea = reply1.replace("thea", "[[THEIuh]]")
checkThea = checkThea.replace("Thea", "[[THEIuh]]")

espeak.synth("%s %s %s, %s %s" %(prefix, message1[1], checkThea, message2[1], reply2))

while 1:
	reply = raw_input(">")
	espeak.synth("%s %s" %(prefix, reply))

