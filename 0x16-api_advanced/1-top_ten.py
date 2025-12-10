#!/usr/bin/python3
import requests

def top_ten(subreddit: str) -> None:
    endpoint = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/abdo)"}
    params = {"limit": 10}
    try:
        response = requests.get(endpoint, headers=headers, timeout=10, allow_redirects=False, params=params)
        
        if response.status_code != 200:
            print (None)
            return

        data = response.json()
        if "data" not in data or "children" not in data["data"]:
            print (None)
            return


        posts = data.get("data", {}).get("children", [])
        for post in posts:
            title = post.get("data", {}).get("title", "")
            print(title)
    except (requests.RequestException, ValueError):
        print (None)
        return

