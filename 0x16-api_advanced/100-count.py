#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords
"""
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}
    if after is None:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return
    data = response.json()
    articles = data['data']['children']
    for article in articles:
        title = article['data']['title'].lower()
        for word in word_list:
            if word.lower() in title and not any(ch.isalpha() for ch in title[title.index(word.lower())-1: title.index(word.lower())]) and not any(ch.isalpha() for ch in title[title.index(word.lower())+len(word): title.index(word.lower())+len(word)+1]):
                if word.lower() in count_dict:
                    count_dict[word.lower()] += 1
                else:
                    count_dict[word.lower()] = 1
    after = data['data']['after']
    if after is not None:
        count_words(subreddit, word_list, after, count_dict)
    else:
        sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_count:
            print("{}: {}".format(word, count))
