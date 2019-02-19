#!/usr/bin/env python3

from datetime import datetime
from github3 import authorize
from getpass import getuser, getpass
import importlib

config_file="config.py"

if __name__ == '__main__':
	try:
		importlib.import_module(config_file.split('.')[0])
		from config import *
	except:
		config = {}
		None

	if len(config) == 0:
		# not setup
		gist_id = input("gist id for ical(eg: e88148cfcfc908de060a456819830cf9): ")
		user = input("github user name: ")
		password = getpass('Password for {0}: '.format(user))

		note = 'xinmedia' + datetime.utcnow().strftime("%F%T")
		note_url = 'http://example.com'
		scopes = ['gist']
		auth = authorize(user, password, scopes, note, note_url)

		config={ 'auth_token': auth.token, 
				 'gist_id': gist_id,
				 'gist_filename': 'xinmedia_bike.ics',
				 'gist_note': note,
				}

		with open(config_file, 'w') as f:
			f.write("config=%s\n"%config)
	else:
			print("already setup, do nothing")
