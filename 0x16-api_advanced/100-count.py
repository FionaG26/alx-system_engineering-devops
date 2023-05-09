#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        hot_list += [child["data"]["title"] for child in data["data"]["children"]]
        after = data["data"]["after"]
        if after is None:
            word_count = {}
            for hot_title in hot_list:
                words = hot_title.lower().split()
                for word in words:
                    word = word.strip(",.!?:;")
                    if word in word_list:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
            for word in sorted(word_count, key=lambda x: (-word_count[x], x)):
                print("{}: {}".format(word, word_count[word]))
        else:
            count_words(subreddit, word_list, hot_list, after)
    else:
        return None
