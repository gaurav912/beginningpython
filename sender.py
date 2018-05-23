#!/usr/bin/env python
import socket
import thread
import base64

rec_ip='127.0.0.1'
rec_port=9999

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((rec_ip,rec_port))

def msg_send():
   while True:
	data=raw_input('Enter msg : ')
	encrypted_data=base64.b64encode(data)
	s.sendto(encrypted_data,('127.0.0.1',8888))
	


def msg_recv():
   while True:
	data2=s.recvfrom(1000)
	decrypted_data=base64.b64decode(data2[0])
	print '\n\t\t\t\t'+data2[1][0]+' : ' +decrypted_data


thread.start_new_thread(msg_send,())
thread.start_new_thread(msg_recv())

while True:
	pass

