#!/usr/bin/python3
"""Get top 10 subreddit posts."""
import requests


def top_ten(subreddit):
    """sbureddit top 10 posts"""
    url = "https://www.reddit.com/r/{}/top.json".format(subreddit)
    resp = requests.get(url, headers={"User-Agent": "mir"})
    if resp.status_code == 200:
        posts = resp.json().get("data").get("children")
        count = 0
        for post in posts:
            if count == 10:
                break
            print(post.get("data").get("title"))
            count += 1
    else:
        print("None")
