#!/usr/bin/python3

# python code for controlling synaccess NP-02B 2 outlet power switch
# in order for the controls to execute, we must receive the returned data on port 2048

import sys
import time
import socket

TCP = "[device IP address]"
TCP_PORT = 23

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

code = sys.argv[1]

if code == 'oneON':
        data = '$A3 1 1\r'
        s.connect((TCP, TCP_PORT))
        ack = s.recv(2048)
        time.sleep(0.5)
        s.sendall(data.encode())
        msg = s.recv(2048)
        s.close()

elif code == 'oneOFF':
        data = '$A3 1 0\r'
        s.connect((TCP, TCP_PORT))
        ack = s.recv(2048)
        time.sleep(0.5)
        s.sendall(data.encode())
        msg = s.recv(2048)
        s.close()
        
if code == 'twoON':
        data = '$A3 2 1\r'
        s.connect((TCP, TCP_PORT))
        ack = s.recv(2048)
        time.sleep(0.5)
        s.sendall(data.encode())
        msg = s.recv(2048)
        s.close()

elif code == 'twoOFF':
        data = '$A3 2 0\r'
        s.connect((TCP, TCP_PORT))
        ack = s.recv(2048)
        time.sleep(0.5)
        s.sendall(data.encode())
        msg = s.recv(2048)
        s.close()
        
if code == 'allON':
        data = '$A7 1\r'
        s.connect((TCP, TCP_PORT))
        ack = s.recv(2048)
        time.sleep(0.5)
        s.sendall(data.encode())
        msg = s.recv(2048)
        s.close()

elif code == 'allOFF':
        data = '$A7 0\r'
        s.connect((TCP, TCP_PORT))
        ack = s.recv(2048)
        time.sleep(0.5)
        s.sendall(data.encode())
        msg = s.recv(2048)
        s.close()
else:
        quit()
