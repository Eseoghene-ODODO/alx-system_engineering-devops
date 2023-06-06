#!/usr/bin/python3
"""
recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as javascript,
but java should not).
"""
import requests
import re


def count_words(subreddit, word_list, counts={}, after=None):
    """
    Prints a sorted count of given keywords in the titles of all hot posts
    for a given subreddit
    """
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
            # Iterate over the titles of the current page and count the
            # keywords
            for post in data.get("children", []):
                title = post.get("data", {}).get("title", "").lower()
                for word in word_list:
                    word = word.lower()
                    # Use regex to match whole words only
                    pattern = r"\b{}\b".format(word)
                    matches = re.findall(pattern, title)
                    # Update the counts dictionary with the number of matches
                    if matches:
                        counts[word] = counts.get(word, 0) + len(matches)
            # Get the next page token
            after = data.get("after")
            # If there is a next page, recursively call the function with the
            # new token
            if after:
                return count_words(subreddit, word_list, counts, after)
            # If there is no next page, print the sorted counts by descending
            # value and ascending key
            else:
                for word, count in sorted(
                        counts.items(), key=lambda x: (-x[1], x[0])):
                    print("{}: {}".format(word, count))
    # If not a valid subreddit or other errors, print nothing
    return None
