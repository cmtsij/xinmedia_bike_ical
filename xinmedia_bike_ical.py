#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup

year="2019"

r = requests.get('https://solomo.xinmedia.com/bike/events/'+ year +'?status=0&style=text')
soup = BeautifulSoup(r.text, features='lxml')

div=soup.select_one('.md_textList')

event_list = []

for ul in div.find_all('ul'):
	if ul.has_attr('class'):
		continue
	
	try:
		event = {}
		
		li=ul.find_all('li')
		date=li[0].text.replace('/','') #mmdd or mmdd-mmdd
		url="https:"+li[1].find('a')['href']
		title=li[1].text.replace('\n','')
		status=li[3].text
		#
		if '-' in date:
			start, end = date.split('-')
		else:
			start = date
			end = date
		start=year+start
		end=year+end

		event['start'] = start
		event['end'] = end
		event['url'] = url
		event['title'] = title
		event['status'] = status
		
		event_list.append(event)
	except:
		continue

ical=[]
ical.append(
'''BEGIN:VCALENDAR
VERSION:2.0
TZID:Asia/Taipei'''
)

for event in event_list:
	ical.append('BEGIN:VEVENT')
	ical.append('SUMMARY:' + event['title'] + '[%s]'%event['status'])
	ical.append('DTSTART;VALUE=DATE:' + event['start'])
	ical.append('DTEND;VALUE=DATE:' + event['end'])
	ical.append('DESCRIPTION:' + event['url'])
	ical.append('END:VEVENT')

ical.append('''END:VCALENDAR''')

ical_text = '\n'.join(ical)





