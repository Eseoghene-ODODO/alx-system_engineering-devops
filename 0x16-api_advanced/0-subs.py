#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns the
number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    # Set the custom User-Agent header
    headers = {"User-Agent": "Bing"}
    # Make a GET request to the subreddit's about.json endpoint
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Check the status code and the response data
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            # Return the number of subscribers
            return data.get("subscribers", 0)
    # Return 0 for invalid subreddit or other errors
    return 0
