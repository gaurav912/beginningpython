#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

page=requests.get('https://en.wikipedia.org/wiki/Web_scraping')
data=page.text
search=BeautifulSoup(data,'html.parser')
sfin=search.find(class_='BodyText')
fin=sfin.find_all('a')
print fin
'''
for i in fin:
	print i
	
'''

