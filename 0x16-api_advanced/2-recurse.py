#!/usr/bin/python3
""" Module to query the Reddit API """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Function that returns top ten posts in a
    subreddit recursively.
    """
    headers = {"User-Agent": "My Reddit Script"}

    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(
            subreddit, after)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:

        data = response.json()

        posts = data["data"]["children"]

        for post in posts:

            title = post["data"]["title"]

            hot_list.append(title)

        after = data["data"]["after"]

        if after:
            recurse(subreddit, hot_list, after)

        return hot_list

    else:
        return(None)
