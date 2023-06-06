#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and prints the
titles of the first 10 hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""
    # Set the custom User-Agent header
    headers = {"User-Agent": "Bing"}
    # Make a GET request to the subreddit's hot.json endpoint with a limit of 10
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    # Check the status code and the response data
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            # Iterate over the children list and print the titles
            for post in data.get("children", []):
                print(post.get("data", {}).get("title", ""))
    else:
        # Print None for invalid subreddit or other errors
        print(None)
