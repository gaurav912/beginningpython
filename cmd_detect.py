#!/usr/bin/env python
import subprocess
ch=raw_input('Enter data : ')

list=ch.split()
for i in list:
	a=subprocess.call(ch,shell=True)
	if a==127:
		print 'SORRY !'+ i.upper() +' is not a shell command ..'
	else:
		print 'CONGRATS !'+ i.upper() + ' is a shell command...'
	print '-----------------------------------------------------------------'

