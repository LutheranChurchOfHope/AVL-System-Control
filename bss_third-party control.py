#!/usr/bin/python3

# use this code sample to run bss third party control from python3 on a linux server

import sys
import socket
import time

from datetime import datetime

TCP = '[IP Address]"
# if there are multiple devices, it still can be the same IP address for all devices
TCP_PORT = 1023

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# here will will define all the variables to be used for the individual third party command hex codes
# we created variables for every fader, mute switch, source selector, etc

specified_control1 = b'[hex code copied directly from audio architect design file third party controller block]'
specified_control2 = b'[hex code copied directly from audio architect design file third party controller block]'
specified_control3 = b'[hex code copied directly from audio architect design file third party controller block]'
specified_control4 = b'[hex code copied directly from audio architect design file third party controller block]'

# ingest a basic argument to tell us what we want to do
cmd = sys.argv[1]

# what did he say?
# I think it was 'blessed are the cheesemakers'

# here we are going to define a log file to be written to an html directory at each triggered event
def log(txt):
	date = datetime.now().strftime("%H:%M_%m/%d/%y")
	f = open('/var/www/html/log/bss-automation'+'.log', "a")
	f.write(date +'\tcommand=['+ cmd + ']\t\t'+ txt +'\r\n')
	f.close

# everything else from here on out is conditional statements
if cmd == 'controlthis':
	log('controlled this')
	s.connect((TCP, TCP_PORT))
	s.send(specified_control1)
	s.send(specified_control2)
	s.close()

elif cmd == 'controlthat':
  elif cmd == 'hallmute':
	log('controlled that')
	s.connect((TCP, TCP_PORT))
	s.send(specified_control3)
	s.send(specified_control4)
	s.close()

else:
  log('no match for event')
