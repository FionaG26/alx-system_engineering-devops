#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords.
"""
import requests

def count_words(subreddit, word_list, count_dict=None, after=None):
"""
Queries the Reddit API recursively, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""
# Initialize count_dict if it's not already initialized
    if count_dict is None:
    count_dict = {}
    for word in word_list:
    count_dict[word.lower()] = 0
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

# Make request to Reddit API
response = requests.get(url, headers=headers, allow_redirects=False, params={'after': after})

# Check if subreddit is valid and response was successful
if response.status_code != 200:
    return

# Parse response json
response_json = response.json()

# Get list of articles from response
articles = response_json['data']['children']

# Loop through each article and update count_dict with occurrences of each word in word_list
for article in articles:
    title_words = article['data']['title'].lower().split()
    for word in word_list:
        count_dict[word.lower()] += title_words.count(word.lower())

# Check if there are more articles to process
if response_json['data']['after'] is not None:
    count_words(subreddit, word_list, count_dict, response_json['data']['after'])
else:
    # Sort count_dict by count (descending) and then alphabetically (ascending)
    sorted_words = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    # Print results for words with non-zero counts
    for word, count in sorted_words:
        if count > 0:
            print('{}: {}'.format(word, count))
