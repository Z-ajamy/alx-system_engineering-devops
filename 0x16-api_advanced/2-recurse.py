#!/usr/bin/python3
"""
Function to query a list of all hot posts on a given Reddit subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
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
    # Define the URL for accessing the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set a custom User-Agent to avoid rate-limiting by the Reddit API
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Set the parameters to paginate the results and retrieve up to 100
    # posts per request
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Send a GET request to the Reddit API
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    # Check if the subreddit is invalid or does not exist
    if response.status_code == 404:
        return None

    # Extract the data from the JSON response
    results = response.json().get("data")

    # Get the 'after' value for pagination
    after = results.get("after")

    # Update the count with the number of posts retrieved in this batch
    count += results.get("dist")

    # Iterate through the list of posts and add the title of each
    # to the hot_list
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # If there is a next page, recursively call the function to get more posts
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the complete list of hot post titles
    return hot_list
