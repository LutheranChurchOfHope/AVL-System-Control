#!/usr/bin/python3

# this is some improved code stuff figured out for controlling multiple IP network 
# projectors and monitor TV's of different makes and models throughout a large facility
# all by populating variables.  .cgi stuff called for using with web control.

import cgitb
import time
import datetime
cgitb.enable()
import socket
import sys

print ("content-Type: text/html")
print ("")

# identify all your devices IP addresses as individual variables
PJ1IP = '192.168.0.10'
PJ2IP = '192.168.0.11'

# a few basic models of projectors, TV's, and their command structures
# add models, commands, and IP ports as needed and populate the variables

PANA_PORT = 4352
PANA_PJON = b'%1POWR 1\r'
PANA_PJOFF = b'%1POWR 0\r'
BARCO_PORT = 9090
BARCO_PJON = b'{"jsonrpc":"2.0","method":"system.poweron","params":{},"id":12}'
BARCO_PJOFF = b'{"jsonrpc":"2.0","method":"system.poweroff","params":{},"id":12}'
SAMSUNG_PORT = 1515
SAMSUNG_ON = b'\xAA\x11\xFE\x01\x01\x11'
SAMSUNG_OFF = b'\xAA\x11\xFE\x01\x00\x10'
SONY_PORT = 20060
SONY_ON = b'*SNPOWR0000000000000001'
SONY_OFF = b'*SNPOWR0000000000000000'

# here we define a variable to ingest a single argument
cmd = sys.argv[1]

# this is the subroutine for the IP connection and data send
# some panasonic projectors require two off commands to be sent, in that case we copy/paste this function with a new name, 
# give it a time.sleep after the incoming message is received, and re-send the off command.
def PJ(pj, port, command, loc):
	try:
		s = socket.socket(socket.AF_INET, soket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((pj, port))
		s.sendall(command)
		msg = s.recv(port)
		print(loc, msg)
	except socket.error as e:
		print(loc, e)
	s.close()
	return()

# to execute commands from the ingested cgi argument, call the defined function and insert variables or quoted strings as needed (IP Address, Port#, command, location)
# I added the location as a python object to print to the output for logging purposes, making troubleshooting a little easier. To prevent huge power surges
# we use a time.sleep command between each on command sent, so the inrush current does not overload any main breakers.  This feature is not required during
# power off sequences.

if cmd == "allon":
	PJ(PJ1IP, PANA_PORT, PANA_PJON, 'room 1')
	time.sleep(1)
	PJ(PJ2IP, BARCO_PORT, BARCO_PJON, 'room 2')

elif cmd == "alloff":
	PJ(PJ1IP, PANA_PORT, PANA_PJOFF, 'room 1')
	PJ(PJ2IP, BARCO_PORT, BARCO_PJOFF, 'room 2')
else:
	print('no match for command')
