from espeak import espeak
from datetime import datetime
t = datetime.now().strftime("%k %M")

message1 = "What is your name?"
message2 = "How old are you?"

print message1,
reply1 = raw_input()

print message2,
reply2 = raw_input()


prefix = "Hello world      "

checkThea = reply1.replace("thea", "THEI uh")

espeak.synth("%s Hello %s, you are %s " %(prefix, checkThea, reply2))
