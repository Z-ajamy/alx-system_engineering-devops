#!/usr/bin/python3
"""
Module to query the Reddit API and return the number of subscribers
for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If an invalid subreddit is given,
    returns 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    # Define the URL for the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {"User-Agent":
               "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
