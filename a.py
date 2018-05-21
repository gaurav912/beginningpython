#!/usr/bin/python

t=()
l=[]
print 'Enter 5 elements which can be of anytype :'

#....taking inputs in list.....
for j in range(0,5):
  l.append(raw_input())

#typecasting list to touple
t=tuple(l)  


#checking the string locations and its substring
for i in range(0,5):
      if type(t[i])==str:
	 if 'ca' in t[i]:
	   print 'The substring ca is present in ' + t[i] + ' and lies in position ' + str(i+1)
	

