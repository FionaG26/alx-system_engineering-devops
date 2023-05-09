#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.

    Returns:
        None.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            for child in children:
                print(child.get("data").get("title"))
        else:
            print("No data found.")
    elif response.status_code == 302:
        print("None")
    else:
        print("Error: {}".format(response.status_code))


if __name__ == "__main__":
    subreddit = input("Enter the name of the subreddit to search: ")
    top_ten(subreddit)
