#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, after=None, count={}):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    # Base case: no more pages to parse
    if after is None and count:
        # Sort the count dictionary by value (descending) and key (ascending)
        sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        # Print the results
        for word, freq in sorted_count:
            print("{}: {}".format(word, freq))
        return

    # Set the base URL and headers for the API request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:holberton.task:v1.0"}

    # Add the after parameter if given
    if after:
        url += "?after={}".format(after)

    # Make the request and get the JSON response
    response = requests.get(url, headers=headers).json()

    # Get the list of posts (children) and the next page (after) from the
    # response
    posts = response.get("data", {}).get("children", [])
    after = response.get("data", {}).get("after", None)

    # Loop through each post and get the title
    for post in posts:
        title = post.get("data", {}).get("title", "").lower()
        # Loop through each word in the word_list and check if it appears in
        # the title
        for word in word_list:
            word = word.lower()
            # Count the number of occurrences of the word in the title
            occurrences = title.split().count(word)
            # Update the count dictionary with the word and its frequency
            if occurrences > 0:
                count[word] = count.get(word, 0) + occurrences

    # Recursively call the function with the next page and the updated count
    return count_words(subreddit, word_list, after, count)
