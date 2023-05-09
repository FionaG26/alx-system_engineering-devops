#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit

    subreddit: A string representing the subreddit to query

    Return: The number of subscribers to the subreddit, or 0 if the subreddit is invalid
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/58.0.3029.110 Safari/537.36'}

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    if data:
        return data.get("subscribers", 0)
    else:
        return 0
