#!/usr/bin/python3
"""Get top 10 subreddit posts."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """sbureddit hot titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"count": count, "after": after, "limit": 100}
    resp = requests.get(url, headers={"User-Agent": "mirayur"}, params=params)

    if resp.status_code == 404:
        return None
    content = resp.json().get("data")
    after = content.get("after")
    count += content.get("dist")
    for post in content.get("children"):
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
