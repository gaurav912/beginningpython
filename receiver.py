#!/usr/bin/env python
import socket
import thread
import base64

rec_ip='127.0.0.1'
rec_port=8888

#Defining ip type and port no
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#Binding ip and port to create socket
s.bind((rec_ip,rec_port))


def recv_msg():
   while True:
	rdata=s.recvfrom(100)
	decrypted_data=base64.b64decode(rdata[0])
	print '\n\t\t\t\t'+rdata[1][0] +' : '+ decrypted_data
	#send_msg(rdata[1])

def send_msg():
   while True:
	r=raw_input("Enter msg: ")
	encrypted_data=base64.b64encode(r)
	s.sendto(encrypted_data,('127.0.0.1',9999))


thread.start_new_thread(recv_msg,())
thread.start_new_thread(send_msg,())

while True:
	pass
