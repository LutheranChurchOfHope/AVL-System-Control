#!/usr/bin/python3

# python code for controlling multiple kipro recorders
# sample transport URL as follows
# http://[kiproaddr]/config?action=set&paramid=eParamID_TransportCommand&value=1&configid=0
# modify number following 'value' to the number which corresponds to the desired transport function
# ingesting the 2 separate arguments allows this code to control mutliple kipro devices
# for more information you can type "http://[kipro_IP ADDRESS]/descriptors" and you will find a full list of the URL commands
# example to ask kipro 1 to record: "./kipro.py 1 record"

import urllib.request as urllib2
import time
import sys

host=sys.argv[1]
cmd=sys.argv[2]

if host == "1":
  HOST = "[IP Address kipro 1]
elif host == "2":
  HOST = "[IP Address kipro 2]
else:
  quit()

# Transport Commands
data = "config?action=set&paramid=eParamID_TransportCommand&value="
record = "3"
stop = "4"

# change media state
data3 = "config?action=set&paramid=eParamID_MediaState&value="
recplay = "0"
datalan = "1"

# end string
data4 = "&configid=0"

if cmd == 'record':
  # first apply media state rec-play in case it was left in data-lan state
  contents = urllib2.urlopen(HOST+data3+recplay+data4).read()
  time.sleep(1) 
  contents = urllib2.urlopen(HOST+data+record+data4).read()

elif cmd == 'stop':
  contents = urllib2.urlopen(HOST+data+stop+data4).read()

else:
  quit()
