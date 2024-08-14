#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list of titles of hot articles
    for a given subreddit. If no results are found, returns None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        children = data.get('children')
        hot_list.extend([child.get('data').get('title') for child in children])
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
