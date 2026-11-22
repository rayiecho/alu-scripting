#!/usr/bin/python3
"""Module that recursively collects the titles of all hot posts."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot posts for a given subreddit.

    Uses Reddit's pagination ('after') and calls itself for each page.
    Returns None if the subreddit is invalid or has no results.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {
        "User-Agent": "linux:alu-scripting.api_advanced:v1.0 (by /u/ayiecho)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return hot_list if hot_list else None
    data = response.json().get("data", {})
    titles = [post.get("data", {}).get("title")
              for post in data.get("children", [])]
    hot_list = hot_list + titles
    after = data.get("after")
    if after is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, after)
