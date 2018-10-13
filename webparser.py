#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs4
import time
def post_finder(subreddit):
    

    url = 'https://new.reddit.com/r/'+subreddit+'/top/?t=all'

    headers = {'user-agent':'crawler for programming resources from subreddits porterwisnie resourcesmaster'}

    r = requests.get(url,headers=headers)

    soup = bs4(r.text,'lxml')

    all_outbound_links = [i.get('href') for i in soup.find_all('a')]

    post_links = []

    for link in all_outbound_links:
        if 'comments' in link and 'http' in link:
            post_links.append(link)
    print(post_links)
    time.sleep(2)

subreddits_to_crawl = ['learnpython','java','Python']

for sub in subreddits_to_crawl:
    post_finder(sub)
