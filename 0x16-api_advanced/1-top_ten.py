#!/usr/bin/python3
"""
Function to print hot posts on a given Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    # Define the URL for accessing the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set a custom User-Agent to avoid rate-limiting by the Reddit API
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Set the parameters to limit the number of posts retrieved to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the subreddit is invalid or does not exist
    if response.status_code == 404:
        print("None")
        return

    # Extract the data from the JSON response
    results = response.json().get("data")

    # Iterate through the list of posts and print the title of each
    [print(c.get("data").get("title")) for c in results.get("children")]
