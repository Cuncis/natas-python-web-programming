#!/usr/bin/env python

import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = "http://%s.natas.labs.overthewire.org" % username

response = requests.get(url, auth=(username, password))

content = response.text

print(content)
# print(re.findall("<pre>\n(.*)\n</pre>", content)[0])
