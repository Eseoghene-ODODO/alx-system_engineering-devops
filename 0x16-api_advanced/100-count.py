#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all hot
articles
"""
import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """A recursive function that queries the Reddit API and prints a sorted
    count of given keywords"""
    # Initialize the count dictionary if it is None
    if count_dict is None:
        count_dict = {}
        for word in word_list:
            count_dict[word.lower()] = 0
    
    # Set the base URL and the headers for the API request
    base_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "python3:count_words:v1.0 (by /u/bing)"}
    
    # Add the after parameter if it is not None
    if after is not None:
        base_url += "?after={}".format(after)
    
    # Make the API request and get the JSON response
    response = requests.get(base_url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()
    
    # Get the list of hot articles
    articles = data["data"]["children"]
    
    # Loop through each article and parse the title
    for article in articles:
        title = article["data"]["title"].lower()
        
        # Loop through each word in the word list and count the occurrences
        # in the title
        for word in word_list:
            word = word.lower()
            count = title.split().count(word)
            count_dict[word] += count
    
    # Get the next page of articles if there is one
    after = data["data"]["after"]
    
    # If there is no more page, print the sorted count of keywords and return
    if after is None:
        # Sort the count dictionary by value (descending) and then by key 
        # (ascending)
        sorted_count = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
        
        # Print only the words that have a positive count
        for word, count in sorted_count:
            if count > 0:
                print("{}: {}".format(word, count))
        return
    
    # Otherwise, recursively call the function with the next page and the
    # updated count dictionary
    else:
        return count_words(subreddit, word_list, after, count_dict)
