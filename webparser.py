#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs4

url = 'https://new.reddit.com/r/learnpython/top/?t=all'

headers = {'user-agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0'}

r = requests.get(url,headers=headers)

soup = bs4(r.text,'lxml')

for link in soup.find_all('a'):
    print(link.get('href'))
