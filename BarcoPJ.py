#!/usr/bin/python3
# this code snippet includes a small update allowing for individual devices to exist as populated variable tables, then called for specifically
# in the conditional statements. Adding different devices and their associated TCP Ports and control command codes is done by adding variables to the list
# Using the Try/Except as part of the on/off subroutine allows a script calling multiple displays to continue operating in the event of connection timeout
# from an individual TCP connected device.

import socket
import sys

PJ1 = '192.168.0.1'

# Barco projectors communicate on port 9090 as a steady stream of data.  The only "ack" that a Barco projector will return is in the case that the command sent 
# meets the complete structure requirement of their json scripting with no <CR> or <LF> sent.  Only the simple ASCII text as shown below.

BARCO_PORT = 9090
BARCO_PJON = b'{"jsonrpc":"2.0","method":"system.poweron","params":{},"id":12}'
BARCO_PJOFF = b'{"jsonrpc":"2.0","method":"system.poweroff","params":{},"id":12}'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cmd = sys.argv[1]

def PJON(pj, port, command):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((pj, port))
		s.sendall(command)
		msg = s.recv(port)
		print(msg)
		time.sleep(1)
	except socket.error as e:
		print(e)
	s.close()
	return()

def PJOFF(pj, port, command):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect((pj, port))
		s.sendall(command)
		msg = s.recv(port)
		print(msg)
		time.sleep(1)
		s.sendall(command)
		print(loc, msg)
	except socket.error as e:
		print(e)
	s.close()
	return()

if cmd == "pjon":
  PJON(PJ1, BARCO_PORT, BARCO_PJON)

if cmd == 'pjoff":
  PJOFF(PJ1, BARCO_PORT, BARCO_PJOFF)

  
