#!/usr/bin/python3
"""
Defines the recurse function.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API for all hot articles of a subreddit.

    subreddit (str): The subreddit to query.
    hot_list (list): A list to store the titles of the hot articles.
    after (str): A token for pagination.

    Returns:
        If the subreddit exists, the function returns the hot_list.
        Otherwise, the function returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data')
    after = data.get('after')

    children = data.get('children')
    for child in children:
        hot_list.append(child.get('data').get('title'))

    if after is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
