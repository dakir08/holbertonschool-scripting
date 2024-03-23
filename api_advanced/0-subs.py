#!/usr/bin/python3
"""
0-subs
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API for the number of subscribers to a given subreddit.

    :param subreddit: The name of the subreddit to query.
    :return: The number of subscribers if valid, 0 otherwise.
    """
    # Define the URL for the subreddit's information using Reddit's API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid getting blocked by Reddit's API for too many requests
    # headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        # response = requests.get(url, headers=headers, allow_redirects=False)
        response = requests.get(url, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('subscribers', 0)
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
