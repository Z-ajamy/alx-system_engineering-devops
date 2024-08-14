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
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Set a custom User-Agent to avoid rate-limiting by the Reddit API
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Set the parameters to limit the number of posts retrieved to 10
    params = {
        "limit": 10
    }

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if the response is successful (status code 200)
        if response.status_code != 200:
            print("None")
            return

        # Check if the response content type is JSON
        if 'application/json' not in response.headers.get('Content-Type', ''):
            print("None")
            return

        # Extract the data from the JSON response
        results = response.json().get("data", {})

        # If results are empty, print None
        if not results:
            print("None")
            return

        # Iterate through the list of posts and print the title of each
        children = results.get("children", [])
        if not children:
            print("None")
            return

        for post in children:
            print(post.get("data", {}).get("title", ""))

    except requests.RequestException as e:
        # Handle any request-related errors
        print(f"An error occurred: {e}")
        print("None")
