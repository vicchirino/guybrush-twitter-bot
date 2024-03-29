#!/usr/bin/env python
# guybrush-twitter-bot/guybrush_threepwood_quotes_bot.py

import requests
from requests_oauthlib import OAuth1
import os
import random

consumer_key = os.environ.get('TWITTER_BOT_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_BOT_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_BOT_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_BOT_ACCESS_TOKEN_SECRET')

def random_quote():
	lines=open(r'quotes.txt').read().splitlines()
	return random.choice(lines)

def format_quote(quote):
    return {'text': '{}'.format(quote)}


def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
    return auth

def post_tweet(payload):
    url = 'https://api.twitter.com/2/tweets'
    auth = connect_to_oauth(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    return requests.post(
            auth=auth, url=url, json=payload, headers={'Content-Type': 'application/json'}
        )

def main():
    quote = random_quote()
    payload = format_quote(quote)
    print(f'## Quote: {quote}')
    try: 
        request = post_tweet(payload)
        print("Tweet posted OK")
    except:  
        print(f'Error: {request.status_code}: {request.reason}')
    
if __name__ == '__main__':
    main()

