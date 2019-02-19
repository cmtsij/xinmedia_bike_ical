#!/usr/bin/env python3
import requests
from github3 import login
from config import *

token = config['auth_token']
gist_id = config['gist_id']
gist_filename = config['gist_filename']

gh = login(token=token)

gist = gh.gist(gist_id)

with open(gist_filename, 'r') as file:
	content = file.read()
	gist.edit("",{gist_filename:{'content':content}})

# force raw upate
raw_url = 'https://gist.github.com/raw/'+gist_id+'/raw/' + gist_filename
requests.get(raw_url)
print('ical_url: ' + raw_url)
