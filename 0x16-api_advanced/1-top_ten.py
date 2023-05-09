#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts listed
for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
    else:
        print(None)
