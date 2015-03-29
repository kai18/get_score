#!/usr/bin/python
from gi.repository import Notify
from bs4 import BeautifulSoup
import urllib.request
from time import sleep
from time import sleep
import sys
def notification(score):
 	Notify.init("Hello World")
 	msg=Notify.Notification.new(score)
 	msg.show()
def get_score():
	url='http://static.cricinfo.com/rss/livescores.xml'
	while True:
		try:
			con=urllib.request.urlopen(url)
			cont=con.read()
			soup=BeautifulSoup(cont)
			data=soup.find_all("description")
			print(data)
			for i in range(len(data)):
				score=data[i].get_text()
				notification(score)
				sleep(20)
		except:
			msg="Error"
			notification(msg)
			sys.exit()
		sleep(20)
			
get_score()

