#!/usr/bin/python3
""" Module to query the Reddit API """

import requests
import requests.auth


def number_of_subscribers(subreddit):
    """ Function that gives the number of subscribers
    in a subreddit.
    """
    client_auth = requests.auth.HTTPBasicAuth('DMIGUkVh_PwUgc6rtLzJBA',
                                              '2T2VPdBleJFmc-KayPse4RD6o839fw')

    post_data = {"grant_type": "password", "username": "proudprune",
                 "password": "naruto95"}

    headers = {"User-Agent": "ChangeMeClient/0.1 by proudprune"}

    url = (f"https://www.reddit.com/r/{subreddit}/about.json")

    response = requests.get(url, auth=client_auth, data=post_data,
                            headers=headers)

    if response.status_code == 200:
        data = response.json()
        subs = data["data"]["subscribers"]
        return subs

    else:
        return False
