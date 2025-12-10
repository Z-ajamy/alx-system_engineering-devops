#!/usr/bin/python3
"""Reddit recursive hot posts fetcher.

This module provides functionality to recursively fetch all hot post titles
from a subreddit using pagination through the Reddit JSON API.
"""

import requests


def recurse(subreddit: str, hot_list: list=None, after: str=None) -> list:
    """Recursively retrieve all hot post titles from a subreddit.
    
    Uses recursive pagination to fetch all hot posts from a subreddit by
    following the 'after' parameter in the Reddit API response. Continues
    until all posts are retrieved or an error occurs.
    
    Args:
        subreddit (str): The name of the subreddit (without the /r/ prefix).
        hot_list (list, optional): Accumulator list for post titles across
            recursive calls. Defaults to None (empty list created internally).
        after (str, optional): Reddit pagination token for fetching the next
            page of results. Defaults to None (starts from first page).
    
    Returns:
        list: List of all hot post titles from the subreddit, or None if the
            subreddit doesn't exist, is invalid, or an error occurs.
    
    Raises:
        No exceptions are raised; all errors return None.
    
    Examples:
        >>> posts = recurse('python')
        >>> len(posts)
        150
        >>> posts = recurse('nonexistentsubreddit')
        >>> posts is None
        True
    """
    if not hot_list:
        hot_list = []
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/abdo)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(endpoint, headers=headers, timeout=10, allow_redirects=False, params=params)
        
        if response.status_code != 200:
            return None

        data = response.json()
        if "data" not in data or "children" not in data["data"]:
            return None

        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title", "")
            hot_list.append(title)
        after = data.get("data", {}).get("after", [])
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except (requests.RequestException, ValueError):
        return None
