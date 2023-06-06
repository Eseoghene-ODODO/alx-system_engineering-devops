#!/usr/bin/python3
"""Count words in all hot posts of a given Reddit subreddit."""

import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """Print sorted counts of given words found in hot posts of a subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        counts (dict, optional): The dictionary to store word counts.
        Defaults to None.
        after (str, optional): The parameter for the next page of the
        API results. Defaults to None.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        after = data.get("data", {}).get("after")

        for post in posts:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in word_list:
                word_lower = word.lower()
                if word_lower in title and not any(
                        t.startswith(word_lower)
                        for t in title if t != word_lower):
                    counts[word_lower] = counts.get(word_lower, 0)
                    + title.count(word_lower)

        if after is not None:
            count_words(subreddit, word_list, counts, after)
        else:
            sorted_counts = sorted(
                    counts.items(),
                    key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print(None)


if __name__ == "__main__":
    subreddit = "python"
    word_list = ["python", "java", "javascript"]
    count_words(subreddit, word_list)
