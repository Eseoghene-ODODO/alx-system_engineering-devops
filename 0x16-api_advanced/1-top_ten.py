#!/usr/bin/python3

"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
If not a valid subreddit, prints None.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit.
    If the subreddit is invalid, prints None.
    """
    # Set a custom User-Agent header
    headers = {'User-Agent': 'My Reddit Client'}

    # Make the API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)


if __name__ == '__main__':
    subreddit = 'python'
    top_ten(subreddit)
