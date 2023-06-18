import logging
import time
from requests_oauthlib import OAuth1
import os
import requests
import base64


consumer_key = os.environ.get('TWITTER_BOT_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_BOT_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_BOT_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_BOT_ACCESS_TOKEN_SECRET')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
    return auth

def upload_media(auth, image_data):
    url = 'https://upload.twitter.com/1.1/media/upload.json'
    request_data = {
      # 'media': image_data,
      'media_data': base64.b64encode(image_data),
      'media_category': 'tweet_image',
    }
    req = requests.post(
       url=url,
       data=request_data,
       auth=auth,
    )
    media_id = req.json()['media_id']
    return media_id

def format_media(media_id):
    body = {'text': '', 'media': {'media_ids': [media_id]}}
    return body

def post_tweet(auth, media_id):
    url = 'https://api.twitter.com/2/tweets'
    json = format_media('{}'.format(media_id))
    return requests.post(
            auth=auth, url=url, json=json, headers={'Content-Type': 'application/json'}
        )

def main():
    frame_id = 446
    auth= connect_to_oauth(consumer_key, consumer_secret, access_token, access_token_secret)
    frames_folder = "monkey-island-II"

    while True:
        image= f"/Users/victorchirino/Projects/guybrush-twitter-bot/frames/{frames_folder}/frame-{frame_id}.jpg"
        try:
          file = open(image, 'rb')
        except:
          print(f"Image file not found in {frames_folder}")
          frame_id = 1
          if frames_folder == "monkey-island-I":
            frames_folder = "monkey-island-II"
            continue
          elif frames_folder == "monkey-island-II":
            frames_folder = "monkey-island-III"
            continue
          else:
            frames_folder = "monkey-island-I"
            continue

        image_data = file.read()
        media_id = upload_media(auth, image_data)

        try: 
          request = post_tweet(auth, media_id)
          print("Tweet posted OK")
          frame_id += 1
        except:  
          print('Error', request)

        logger.info("Waiting...")
        time.sleep(60*60*3) # 3 hours

if __name__ == '__main__':
    main()
