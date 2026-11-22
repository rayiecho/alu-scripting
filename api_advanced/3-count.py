#!/usr/bin/python3
"""Module that recursively counts keywords in the titles of hot posts."""
import requests


def print_counts(counts, word_list):
    """Print keyword counts sorted by count (desc), then alphabetically."""
    lowered = [word.lower() for word in word_list]
    totals = {word: counts[word] * lowered.count(word) for word in counts}
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        if total > 0:
            print("{}: {}".format(word, total))


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keyword occurrences in all hot post titles.

    Prints a sorted count of the keywords. Prints nothing if the
    subreddit is invalid or no keywords match.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {
        "User-Agent": "linux:alu-scripting.api_advanced:v1.0 (by /u/ayiecho)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print_counts(counts, word_list)
        return
    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for word in title.lower().split():
            if word in counts:
                counts[word] += 1
    after = data.get("after")
    if after is None:
        print_counts(counts, word_list)
        return
    count_words(subreddit, word_list, after, counts)
