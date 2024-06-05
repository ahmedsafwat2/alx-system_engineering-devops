#!/usr/bin/python3
"""import libraries"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers"""

    try:
        headers = {
            'User-Agent': 'Mahmoud_Elwazeer'
        }
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

        req = requests.get(
            url, headers=headers, allow_redirects=False).json()
        num_subscribe = req.get("data").get("subscribers")
        return (num_subscribe)

        # url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

        # req = requests.get(
        #       url, headers=headers, allow_redirects=False).json()
        # get_data = req.get("data")
        # num_subscribe = get_data.get("children")[-1].get(
        #         "data").get("subreddit_subscribers")
        # return (num_subscrib)

    except Exception:
        return (0)
