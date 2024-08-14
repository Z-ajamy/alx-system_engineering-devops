#!/usr/bin/python3
"""
Function to query a list of all hot posts on a given Reddit subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List to store the titles of hot posts.
        after (str): The identifier of the last post in the current batch,
        used for pagination.
        count (int): The cumulative count of retrieved posts.

    Returns:
        list: A list containing the titles of all hot posts on the subreddit.
              Returns None if the subreddit is invalid.
    """
    if hot_list is None:
        hot_list = []

    print(f"Calling recurse with after={after}, count={count}")  # Debugging

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 404:
            return None
        results = response.json().get("data", {})
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

    after = results.get("after")
    count += results.get("dist", 0)

    for c in results.get("children", []):
        hot_list.append(c.get("data", {}).get("title", ""))

    if after:
        print(f"Recursing with after={after}, count={count}")  # Debugging
        return recurse(subreddit, hot_list, after, count)
    return hot_list
