#!/usr/bin/python3

#this is a basic control for yamaha MRX7D
#please see Yamaha white paper for specific information, this is only a basic code example for correct syntax
#you must first create under 'tools/remote control setup list' individual ID numbers for items you want to control
#the number immediately following "Index" below is the ID number of the item controlled, in this example it is a mute switch
#The complete manual can be found at: 
#https://usa.yamaha.com/files/download/other_assets/1/1144121/mtx_mrx_xmv_ex_remote_control_protocol_spec_v310_en.pdf

import sys
import socket
TCP = '192.168.0.1'
TCP_PORT = 49280

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#in my testing using netcat it appears that the MRX7D would only receive and respond to commands after devmode normal request is first sent

devstatus = b'devstatus runmode\n'
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
