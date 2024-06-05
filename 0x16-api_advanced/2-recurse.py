#!/usr/bin/python3
"""import libraries"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    try:
        headers = {
                'User-Agent': 'Mahmoud_Elwazeer'
            }
        params = {'after': after}
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

        req = requests.get(
            url, headers=headers, params=params,  allow_redirects=False).json()
        get_data = req.get("data")
        after = get_data.get("after")

        data = get_data.get("children")
        for title in data:
            hot_list.append(title.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)

        return (hot_list)

    except Exception:
        return (None)
