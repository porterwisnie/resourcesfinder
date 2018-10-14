#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as bs4
import time
#next step is to find all a tags in each post link

headers = {'user-agent':'crawler for programming resources from subreddits porterwisnie resourcesmaster'}

def post_finder(subreddit):

    url = 'https://new.reddit.com/r/'+subreddit+'/top/?t=all'

    r = requests.get(url,headers=headers)

    soup = bs4(r.text,'lxml')

    all_outbound_links = [i.get('href') for i in soup.find_all('a')]

    post_links = []

    for link in all_outbound_links:
        if 'comments' in link and 'http' in link:
            post_links.append(link)
    return post_links
    time.sleep(2)

def comment_parser():

	for link in post_links:

		r = requests.get(link,headers=headers)

		soup = bs4(r.text,'lxml')

		links_in_posts = [i.get('href') for i in soup.find_all('a')]

		print(links_in_posts)

		time.sleep(2)
subreddits_to_crawl = ['learnpython','java','Python']

for sub in subreddits_to_crawl:
    post_finder(sub)

