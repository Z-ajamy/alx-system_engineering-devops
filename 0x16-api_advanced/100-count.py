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
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "count": count, "limit": 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            word_lower = word.lower()
            word_count = title.count(word_lower)
            if word_count > 0:
                if instances.get(word_lower) is None:
                    instances[word_lower] = word_count
                else:
                    instances[word_lower] += word_count

    if after is None:
        if len(instances) == 0:
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in instances:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)
