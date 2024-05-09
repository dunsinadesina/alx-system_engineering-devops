#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of subscriber"""
from requests import get


def number_of_subscribers(subreddit):
    """Return the total subscribers on a subreddit"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0
    user = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = get(url, headers=user)
    result = response.json()
    try:
        return result.get('data').get('subscribers')
    except Exception:
        return 0
