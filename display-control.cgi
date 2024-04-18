#!/usr/bin/python3

# this is some new and slightly improved code stuff figured out for controlling mulriple IP network 
# projectors and monitor TV's of different makes and models throughout a large facility
# all by populating variables.  .cgi stuff called for using with web control.

import cgitb
import urllib.request as urllib2
import time
import datetime
cgitb.enable()
import socket
import sys

print ("content-Type: text/html")
print ("")

PJIP = '192.168.0.10'

# a few basic models of projectors, TV's, and their command structures

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

# to execute commands from the ingested cgi argument, call the defined function and insert variables as needed (IP Address, Port#, command, location)
# I added the location as a variable for logging purposes, making troubleshooting a little easier.

if cmd == "on":
  PJ(PJIP, PANA_PORT, PANA_PJON, 'somewhere')

elif cmd == "off":
  PJ(PJIP, PANA_PORT, PANA_PJOFF, 'somewhere')

else:
  print('no match for command')
