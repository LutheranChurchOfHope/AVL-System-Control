#!/usr/bin/python3

#this is a basic control for yamaha MRX7D
#please see Yamaha white paper for specific information, this is only a basic code example for correct syntax
#you must first create under 'tools/remote control setup list' individual ID numbers for items you want to control
#the number immediately following "Index" below is the ID number of the item controlled, in this example it is a mute switch

import sys
import socket
TCP = '192.168.0.1'
TCP_PORT = 49280

s = socket.socket(socket.AV_INET, socket.SOCK_STREAM)

devstatus = b'devmode normal\n'
sampleoff = b'set MTX:Index_1 0 0 \"OFF\"\n'

s.connect((TCP, TCP_PORT))
s.send(devstatus)
msg = s.recv(49280)
print(msg)
s.send(sampleoff)
msg1 = s.recv(49280)
print(msg1)
s.close()
quit()
