#!/usr/bin/python3
"""Module that queries the Reddit API for a subreddit's subscriber count."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit.

    If the subreddit is invalid, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu-scripting.api_advanced:v1.0 (by /u/ayiecho)"
    }
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
