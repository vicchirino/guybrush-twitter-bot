import logging
import time
from twitter import Twitter, OAuth
import os

consumer_key = os.environ.get('TWITTER_BOT_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_BOT_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_BOT_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_BOT_ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BARER_TOKEN')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def twitter_Oauth():
  return OAuth(token=access_token,
    token_secret=access_token_secret,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret)

def upload_media(auth, image_data):
    t_up = Twitter(domain='upload.twitter.com', auth=auth)
    media_id = t_up.media.upload(media=image_data)["media_id_string"]
    return media_id


def main():
    frame_id = 4
    auth= twitter_Oauth()
    t = Twitter(auth=auth)
    frames_folder = "monkey-island-I"

    while True:
        image= f"/Users/victorchirino/Projects/guybrush-twitter-bot/frames/{frames_folder}/frame-{frame_id}.jpg"
        try:
          file = open(image, 'rb')
        except:
          print(f"Image file not found in {frames_folder}")
          frame_id = 0
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
          t.statuses.update(media_ids=",".join([media_id]))
          print("Tweet posted OK")
        except:  
          print('Error')

        logger.info("Waiting...")
        frame_id += 1
        time.sleep(60*60*3) # 3 hours

if __name__ == '__main__':
    main()
