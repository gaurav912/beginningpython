#!/usr/bin/env python2
import time
import webbrowser
import datetime

option='''
	  Press 1: Search each word in google
	  Press 2: Search image for each word in google
	  Press 3: Display all url's of google 1st page
	  Press 4: Display current time
	  Press 5: Open default browser
	  Press 6: Display all IP's of connected networks
	  Press 7: Enter domain and get owner details(name,email,contact no)
	'''
print option

ch=raw_input()

if ch=='1':
   take_input=raw_input("Enter anything :")
#taking input from user
   extracted_input=take_input.strip()
#removing leading and training spaces
   final_input=extracted_input.split()
#splitting every words
   for i in final_input:
	webbrowser.open_new_tab('https://www.google.com/search?q='+i)

elif ch=='2':
   take_input=raw_input("Enter anything :")
#taking input from user
   extracted_input=take_input.strip()
#removing leading and training spaces
   final_input=extracted_input.split()
#splitting every words
   for i in final_input:
	webbrowser.open_new_tab('https://www.google.com/search?q='+i+ '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjDsdyN6IrbAhXCXysKHSGQBw4Q_AUoBHoECAEQBg')


elif ch=='3':
   take_input=raw_input("Enter anything :")
#taking input from user
   extracted_input=take_input.strip()
#removing leading and training spaces
   final_input=extracted_input.split()
#splitting every words

elif ch=='4':
   print 'Current time of the system is :'
   print datetime.datetime.now()
   
	
elif ch=='5':
   webbrowser.open('https://www.google.com',new=2, autoraise=True)  

elif ch=='6':
   print 'coming soon.....'

elif ch=='7':
   s=raw_input("Enter the domain name : ")
   

    

	

