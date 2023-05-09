#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and counts the occurrences of
given keywords in the titles of the hot posts of a given subreddit.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Counts the occurrences of given keywords in the titles of the hot posts of
    a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list of str): The list of keywords to count.
        after (str): The Reddit post ID to start the search from.
        word_count (dict): The dictionary to store the count of each keyword.

    Returns:
        None.
    """

    if not word_list:
        # No more keywords to count, print the result
        for word, count in sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0])):
            print('{}: {}'.format(word, count))
        return

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        # Invalid subreddit or other error
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])

    for post in posts:
        title = post.get('data', {}).get('title', '').lower()

        for word in word_list[:]:
            if (' ' + word + ' ') in (' ' + title + ' '):
                # Found a keyword in the title, increment the count
                word_list.remove(word)
                word_count[word] = word_count.get(word, 0) + 1

    if not posts:
        # No more posts to search, print the result
        for word, count in sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0])):
            print('{}: {}'.format(word, count))
        return

    # Recursively search the remaining posts
    count_words(subreddit, word_list, posts[-1]['data']['name'], word_count)
