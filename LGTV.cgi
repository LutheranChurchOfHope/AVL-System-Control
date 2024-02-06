#!/usr/bin/python
# use this code for turning lg TV on or off
# you will need to set up access on the LG TV, it needs to be a commercial series display
# for this code to work, newer consumer displays require an encryption key for the commands
  
import cgitb
import urllib2
import time
from datetime import datetime
import sys
import socket
cgitb.enable()
from wakeonlan import send_magic_packet

print 'content-type: text/html\r\n'

cmd = sys.argv[1]
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

PORT = 9761
lgTVON = 'ka 00 01'
lgTVOFF = 'ka 00 00

if cmd == 'lgtvON':
	send_magic_packet('[Specified TV's MAC Adreess]')

elif cmd == 'lgtvOFF':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(5)
	sock.connect(([Specified TV's IP address], PORT))
	sock.sendall(lgTVOFF + '\r')
	msg = sock.recv(9761)
	print msg
	sock.close()

else:
  print ('no match for command')

  
