#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function should return None
"""

import requests

def recurse(subreddit, hot_list=[], after=""):
    """
    Recursive function that queries the Reddit API for
    hot articles of a given subreddit.
    """
    # Define the base URL for querying hot articles in a subreddit
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'reddit-recursive/0.1'}
    
    params = {} 
    if after:
        params['after'] = after
    
    try:
        response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)
        # If the subreddit is not valid, Reddit API may return a 302 or 404 status code
        if response.status_code in [302, 404]:
            return None
        data = response.json()
        
        # Extract titles of hot articles and add them to the hot_list
        hot_list += [article['data']['title'] for article in data['data']['children']]
        
        # Check for more pages
        after = data['data'].get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        
        print(data)
        return hot_list
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None
