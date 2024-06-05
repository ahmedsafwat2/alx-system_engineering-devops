#!/usr/bin/python3
"""import libraries"""
import requests


def top_ten(subreddit):
    """top ten posts"""
    try:
        headers = {
                'User-Agent': 'Mahmoud_Elwazeer'
            }
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

        req = requests.get(
            url, headers=headers, allow_redirects=False).json()
        get_data = req.get("data").get("children")

        for title in get_data[:10]:
            print(title.get("data").get("title"))

    except Exception:
        print(None)
