#!/usr/bin/python3
"""Get subscribers count."""
import requests


def number_of_subscribers(subreddit):
    """sbureddit subscribers count"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers={"User-Agent": "mir"})
    if resp.status_code == 200:
        data = resp.json().get("data")
        return data.get("subscribers")
    else:
        return 0
