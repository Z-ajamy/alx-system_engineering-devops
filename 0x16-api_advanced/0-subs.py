#!/usr/bin/python3
"""Reddit subreddit subscriber counter.

This module provides functionality to fetch the number of subscribers for any
public subreddit using the Reddit JSON API.
"""

import requests


def number_of_subscribers(subreddit: str) -> int:
    """Retrieve the subscriber count for a given subreddit.
    
    Queries the Reddit JSON API to fetch the number of subscribers for a
    specified subreddit. Returns 0 if the subreddit doesn't exist, is private,
    or if any error occurs during the request.
    
    Args:
        subreddit (str): The name of the subreddit (without the /r/ prefix).
    
    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid,
            inaccessible, or an error occurs.
    
    Raises:
        No exceptions are raised; all errors return 0.
    
    Examples:
        >>> number_of_subscribers('python')
        1234567
        >>> number_of_subscribers('nonexistentsubreddit')
        0
        >>> number_of_subscribers('')
        0
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0
    endpoint = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/abdo)"}
    try:
        response = requests.get(endpoint, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        data = response.json()
        if not data:
            return 0
        return data.get("data", {}).get("subscribers", 0)

    except (requests.RequestException, ValueError):
        return 0
