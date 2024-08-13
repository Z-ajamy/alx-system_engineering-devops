#!/usr/bin/python3
"""
Function to count words in all hot posts of a given Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Dictionary of words and their respective counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter for results matched thus far.
    """
    # Define the URL for accessing the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Set a custom User-Agent to avoid rate-limiting by the Reddit API
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Set the parameters to paginate the results and retrieve up to
    # 100 posts per request
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    # Send a GET request to the Reddit API
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    # Try to parse the response and handle exceptions if the subreddit is
    # invalid
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    # Extract the data from the JSON response
    results = results.get("data")

    # Get the 'after' value for pagination
    after = results.get("after")

    # Update the count with the number of posts retrieved in this batch
    count += results.get("dist")

    # Iterate through the list of posts
    for c in results.get("children"):
        # Get the title of each post, convert it to lowercase, and split into
        # words
        title = c.get("data").get("title").lower().split()

        # Count occurrences of each word in word_list in the title
        for word in word_list:
            if word.lower() in title:
                # Count how many times the word appears in the title
                times = len([t for t in title if t == word.lower()])

                # Update the instances dictionary with the count
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    # Check if there are more posts to retrieve
    if after is None:
        # If no words were found, print an empty line
        if len(instances) == 0:
            print("")
            return

        # Sort the dictionary by count in descending order and by word in
        # alphabetical order
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))

        # Print the word counts
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        # Recursively call the function to get more posts
        count_words(subreddit, word_list, instances, after, count)
