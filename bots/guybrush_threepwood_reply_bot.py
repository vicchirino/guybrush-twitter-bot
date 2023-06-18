#!/usr/bin/env python
# guybrush-twitter-bot/guybrush_threepwood_reply_bot.py

import logging
import time
import os
import requests
from guybrush_threepwood_quotes_bot import post_tweet, random_quote

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class Tweet:
  def __init__(self, id, created_at, text):
    self.id = id
    self.created_at = created_at
    self.text = text

bearer_token = os.environ.get('BARER_TOKEN')

BOT_USER_ID = os.environ.get('BOT_USER_ID')

def create_mentions_url():
    # Replace with user ID below
    user_id = BOT_USER_ID
    return "https://api.twitter.com/2/users/{}/mentions".format(user_id)

def get_mentions_params(since_id):
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at", "since_id": since_id, "max_results": 10}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserMentionsPython"
    return r

def connect_to_endpoint(url, params, method):
    response = requests.request(method, url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def encode_tweet_object(tweet_json):
    tweet = Tweet(id=tweet_json['id'], created_at=tweet_json['created_at'], text=tweet_json['text'])
    print(f'Tweet: {tweet.text}')
    return tweet

def get_mentions(since_id):
    url = create_mentions_url()
    params = get_mentions_params(since_id)
    json_response = connect_to_endpoint(url, params, "GET")
    json_response_array = []

    if 'data' in json_response:
        json_response_array = json_response['data'] 
        print(json_response_array)
    return json_response_array
       

def format_quote(tweet: Tweet):
    return {'text': '{}'.format(random_quote()), 'reply': {'in_reply_to_tweet_id': '{}'.format(tweet.id)}}

def reply_tweet(tweet):
    payload = format_quote(tweet)
    json_response = post_tweet(payload)
    print(json_response)

def answer_tweet(tweet: Tweet):
    print(f'Tweet text: {tweet.text}')
    reply_tweet(tweet)

def check_mentions(since_id): 
    mentions = get_mentions(since_id)
    sorted_mentions = sorted(mentions, key=lambda d: d['id'], reverse=False)

    for tweet_json in sorted_mentions:
        tweet = encode_tweet_object(tweet_json)
        if since_id >= int(tweet.id):
            continue
        answer_tweet(tweet)
        since_id = int(tweet.id)
    
    print(f'Final since_id {since_id}')
    return since_id

def main():
    since_id = 1666839535429517314

    while True:
        since_id = check_mentions(since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()
