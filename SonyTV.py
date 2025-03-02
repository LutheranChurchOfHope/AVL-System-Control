#!/usr/bin/python3

# this is a script for turning on and off sony TV's
# simple IP control with no authentication is required for this code
# This should only be done on closed LANs or with proper firewall protection

import urllib.request as urllib2
import socket
import sys

SONY_PORT = 20060

# some sony TVs do not require \n after the command is sent
SONY_ON = b'*SCPOWR0000000000000001\n'
SONY_OFF = b'*SCPOWR0000000000000000\n'

tv1 = '<Living Room TV IP Address>'
tv2 = '<Kitchen TV IP Address>'


port = 20060

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ingest an argument
cmd = sys.argv[1]

def SONY(tv, port, command, loc):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((tv, port))
		s.sendall(command)
		msg = s.recv(port)
		print(loc, msg)
	except socket.error as e:
		print(loc, e)
	s.close()

if cmd == "on":
        SONY(tv1, SONY_PORT, SONY_ON, 'Living Room ')
        SONY(tv2, SONY_PORT, SONY_ON, 'Kitchen ')
        
if cmd == "off":
        SONY(tv1, SONY_PORT, SONY_OFF, 'Living Room ')
        SONY(tv2, SONY_PORT, SONY_OFF, 'Kitchen ')

else:
        print('no match for command')
        
