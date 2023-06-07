#!/usr/bin/python3
""" Module to query the Reddit API """

import requests


def top_ten(subreddit):
    """ Function that gives top ten posts
    in a subreddit.
    """
    headers = {"User-Agent": "My Reddit Script"}

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:

        data = response.json()

        posts = data["data"]["children"]

        for post in posts:

            title = post["data"]["title"]

            print(title)

    else:
        print(None)
