"""
Most downloaded package, used to get data or information from server or site

HTTP for humans
"""

import requests

r = requests.get('https://xkcd.com/353/')  # response object

# to get an information from an object
# print(dir(r))
# print(help(r))

"""Use html parser to get detailed infor"""
print(r.text)

r2 = requests.get('https://xkcd.com/comics/python.png')

print(r2.content)  # will build byte code

with open('comic.png', 'wb') as f:
    f.write(r2.content)

print(r2.status_code)  # 500 errors are server error

print(r2.ok)  # if less than 400, all good, no server or client error

print(r2.headers)
print(r.headers)

payload = {'page': 2, 'count': 25}

r3 = requests.get('https://httpbin.org/get', params=payload)

user_data = {'username': 'shekhaw', 'password': 'testing'}

r4 = requests.post('https://httpbin.org/post', params=user_data)
print(r4.text)

r5 = r4.json()  # converted output that is in json format to dict
