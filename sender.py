#!/usr/bin/env python
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	data=raw_input('Enter msg to send : ')
	s.sendto(data,('127.0.0.1',8888))
	data2=s.recvfrom(1000)
	print data2[1][0]+' : ' +data2[0]

