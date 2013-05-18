#!/bin/bash
temp=$(/home/pi/tmp102/tmp102.sh)
cat /home/pi/tmp102/blank.json | sed 's/T1/'$temp' /g' > \
/home/pi/tmp102/send.json
curl --request PUT \
--data-binary @/home/pi/tmp102/send.json \
--header "X-ApiKey:ZZZZZ" \
http://api.cosm.com/v2/feeds/XXXXX
