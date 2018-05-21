#!/usr/bin/env python
import socket

rec_ip='127.0.0.1'
rec_port=8888

#Defining ip type and port no
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Binding ip and port to create socket
s.bind((rec_ip,rec_port))

while True:
  rdata=s.recvfrom(100)
  print rdata[1][0] +' : '+ rdata[0]
  r=raw_input("Enter to reply : ")
  s.sendto(r,rdata[1])
  
  
