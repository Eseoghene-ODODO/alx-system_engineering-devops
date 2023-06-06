#!/usr/bin/python3

"""
Queries the Reddit API and returns the number of subscribers for a give
subreddit.
If an invalid subreddit is given, the function returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.
    Returns 0 if the subreddit is invalid.
    """
    # Set a custom User-Agent header
    headers = {'User-Agent': 'My Reddit Client'}

    # Make the API request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0


if __name__ == '__main__':
    subreddit = 'python'
    subscribers = number_of_subscribers(subreddit)
    print(f"The subreddit r/{subreddit} has {subscribers} subscribers.")
