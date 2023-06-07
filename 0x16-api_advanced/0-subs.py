#!/usr/bin/python3
""" Module to query the Reddit API """

import requests


def number_of_subscribers(subreddit):
    """ Function that gives the number of subscribers
    in a subreddit.
    """
    headers = {"User-Agent": "My Reddit Script"}

    url = (f"https://www.reddit.com/r/{subreddit}/about.json")

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        subs = data["data"]["subscribers"]

        return subs

    else:
        return False
