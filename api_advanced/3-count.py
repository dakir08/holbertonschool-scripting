#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
parses the title of all hot articles
and prints a sorted count of given keywords
"""

import requests

def count_words(subreddit, word_list, after="", word_counts={}):
    """
    Recursive function that queries the Reddit API
    """
    if after is None:  # Base case: no more pages to fetch
        if not word_counts:
            return
        # Sort and print the results
        for word in sorted(word_counts, key=lambda w: (-word_counts[w], w)):
            if word_counts[word] > 0:
                print(f"{word}: {word_counts[word]}")
        return
    
    if not word_counts:  # Initialize word counts dictionary
        word_counts = {word.lower(): 0 for word in word_list}
    
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'reddit-wordcount/0.1'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(base_url, headers=headers, params=params, allow_redirects=False)
        if response.status_code in [302, 404]:  # Check for invalid subreddit
            return
        data = response.json()
        articles = data['data']['children']
        
        for article in articles:
            title = article['data']['title'].lower()
            # Count occurrences of each keyword
            for word in word_counts:
                word_counts[word] += title.split().count(word)
        
        # Recurse with the next page token
        count_words(subreddit, word_list, data['data']['after'], word_counts)
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
