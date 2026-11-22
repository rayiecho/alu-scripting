#!/usr/bin/python3
"""Module that prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid, print None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu-scripting.api_advanced:v1.0 (by /u/ayiecho)"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
