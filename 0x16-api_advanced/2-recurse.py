#!/usr/bin/python3
"""
A script the contains arecursive function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should return
None.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts for a given subreddit"""
    # Set the custom User-Agent header
    headers = {"User-Agent": "Bing"}
    # Make a GET request to the subreddit's hot.json endpoint with an after
    # parameter
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )
    # Check the status code and the response data
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            # Append the titles of the current page to the hot_list
            for post in data.get("children", []):
                hot_list.append(post.get("data", {}).get("title", ""))
            # Get the next page token
            after = data.get("after")
            # If there is a next page, recursively call the function with
            # the new token
            if after:
                return recurse(subreddit, hot_list, after)
            # If there is no next page, return the hot_list
            else:
                return hot_list
    # If not a valid subreddit or other errors, return None
    return None
