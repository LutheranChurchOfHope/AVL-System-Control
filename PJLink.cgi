#!/usr/bin/python3

# use this python script in a cgi or www directory to operate a Panasonic PJLink projector
# you can add arguments and variables to make it easier. Panasonic PJLink default port is 4352, it can be changed through the menu tree in the projector
# basic command from URL to turn on projector using this cgi python script: '[server IP Address]/[cgi or whatever sub www directory in your control server]/PJlink.cgi?PJon'
# important note: projector must have no password to at least one of the 'user' or 'admin' logins, or else the data sent will require matched encryption

import cgitb
import time
import socket
import sys
cgitb.enable()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '[Projector IP Address]'

cmd = sys.argv[1]

# to control more than one projector, add a second argument and define variables as the IP Addresses or names of the projector as
# they would appear in DNS

print("content-type: text/html\r\n\r")

if cmd == 'PJon':
	data = '%1POWR 1' + '\r'
	s.settimeout(2)
	time.sleep(0.2)
	s.connect((HOST, PORT))
	ack = s.recv(4352)
	print(ack)
	s.sendall(data.encode())
  msg = s.recv(4352)
  print(msg)
	s.close()

elif cmd == 'PJoff':
	data = '%1POWR 0' + '\r'
	s.settimeout(2)
	time.sleep(0.2)
	s.connect((HOST, PORT))
	ack = s.recv(4352)
	print(ack)
	s.sendall(data.encode())
	msg = s.recv(4352)
  print(msg)
	s.close()

else:
  print('no match for command')
  quit()
