#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited by spaces).
"""

import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API and counts the occurrences of each keyword in the titles
    of the hot articles.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'limit': 100}
    if after:
        params['after'] = after
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    articles = data.get('data', {}).get('children', [])
    if not articles:
        return
    if count_dict is None:
        count_dict = {}
    for article in articles:
        title = article.get('data', {}).get('title', '').lower()
        words = title.split()
        for word in words:
            if not word.isalpha():
                continue
            if word.lower() in word_list:
                if word.lower() not in count_dict:
                    count_dict[word.lower()] = 0
                count_dict[word.lower()] += 1
    after = data.get('data', {}).get('after', None)
    if not after:
        sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print('{}: {}'.format(word, count))
        return
    count_words(subreddit, word_list, after=after, count_dict=count_dict)
