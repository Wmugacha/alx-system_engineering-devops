#!/usr/bin/python3
""" Module to query the Reddit API """

import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """ Function that returns count of keywords in a
    subreddit recursively.
    """

    if word_count is None:
        word_count = {}

    headers = {"User-Agent": "My Reddit Script"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])

        if posts:
            for post in posts:
                title = post.get("data", {}).get("title", "").lower()
                words = title.split()

                for word in words:
                    word = word.rstrip("!,.?_").lower()
                    if word in word_list:
                        word_count[word] = word_count.get(word, 0) + 1

            after = data.get("data", {}).get("after", None)
            if after:
                count_words(subreddit, word_list, after, word_count)
            else:
                sorted_count = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0]))
                for word, count in sorted_count:
                    print(f"{word}: {count}")
    else:
        print(None)
