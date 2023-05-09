#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given
keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, after='', word_count={}):
    """
    Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of
    given keywords.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): A list of keywords to count.
        after (str): The ID of the last post seen in the previous request (default is empty string).
        word_count (dict): A dictionary to store the count of each keyword (default is empty dictionary).

    Returns:
        None.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    if after:
        url += '&after={}'.format(after)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return
    data = r.json()
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        title = post.get('data', {}).get('title', '').lower()
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + title.count(' ' + word.lower() + ' ')
    after = data.get('data', {}).get('after', '')
    if after is None:
        sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words:
            print('{}: {}'.format(word, count))
        return
    count_words(subreddit, word_list, after, word_count)
