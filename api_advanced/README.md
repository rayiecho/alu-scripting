# API advanced

Python scripts that query the Reddit API using the `requests` module.

| File | Description |
| ---- | ----------- |
| `0-subs.py` | Returns the number of subscribers of a subreddit (0 if invalid). |
| `1-top_ten.py` | Prints the titles of the first 10 hot posts of a subreddit (None if invalid). |
| `2-recurse.py` | Recursively returns a list of all hot post titles (None if invalid). |
| `3-count.py` | Recursively counts given keywords in hot post titles and prints a sorted count. |

All requests use a custom User-Agent and do not follow redirects, so
invalid subreddits are detected correctly.
