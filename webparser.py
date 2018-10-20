#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs4
import time

post_links = []

links_in_posts = set()

headers = {'user-agent':'crawler for programming resources from subreddits porterwisnie resourcesmaster'}

def post_finder(subreddit):

    url = 'https://new.reddit.com/r/'+subreddit+'/top/?t=all'

    r = requests.get(url,headers=headers)

    soup = bs4(r.text,'lxml')

    all_outbound_links = [i.get('href') for i in soup.find_all('a')]


    for link in all_outbound_links:
        if 'comments' in link and 'http' in link:
            post_links.append(link)
  
    time.sleep(1.5)

def comment_parser(post):

    for link in post:

        r = requests.get(link,headers=headers)

        soup2 = bs4(r.text,'lxml') 

        for item in soup2.find_all('a'):
            link = item.get('href')
            try:
                if link[0:4] == 'http':
                    links_in_posts.add(link)  
            except:
                pass
        time.sleep(1.5)
    print(links_in_posts)

subreddits_to_crawl = ['learnpython']

for sub in subreddits_to_crawl:
    post_finder(sub)
comment_parser(post_links)
