## Twitter Guybrush Threepwood quotes bot.

A simple Twitter bot that tweets a quote every hour of the mighty pirate, Guybrush Threepwood.
Also reply for mentions with a random quote.

### Guybrush quotes
- The secret of Monkey Island: http://www.gamefaqs.com/pc/562681-the-secret-of-monkey-island/faqs/23891
- The curse of Monnkey Island: https://gamefaqs.gamespot.com/pc/29083-the-curse-of-monkey-island/faqs/60819

### Run the bot

1. Clone the project.
2. Create an environment doing `pip install virtualenv` and then `virtualenv {ENVIRONMENT_NAME}`. 
3. Activate the virtual if needed `source /{ENVIRONMENT_NAME}/bin/activate` (Note: The method used to activate the virtual environment may be different, depending on your operating system and shell. You can learn more about this in the [venv documentation](https://docs.python.org/3/library/venv.html).)
4. Generate the twitter account keys. Visit https://developer.twitter.com.
5. Run the scrirpt for a single tweet `TWITTER_BOT_CONSUMER_KEY='{KEY}' TWITTER_BOT_CONSUMER_SECRET='{KEY}' TWITTER_BOT_ACCESS_TOKEN='{KEY}' TWITTER_BOT_ACCESS_TOKEN_SECRET='{KEY}' python guybrush_threepwood_quotes_bot.py`
6. Run the script for replying mentions `TWITTER_BOT_CONSUMER_KEY='hJJDZCFWBp8dvAkvD9m1wbUof' TWITTER_BOT_CONSUMER_SECRET='AqxpUMkZHJ37tYmQgzl1HFkvcXKO4T6kOE7WoGbsteHVyVDsLC' TWITTER_BOT_ACCESS_TOKEN='1456329931764473864-Unr0RpEqKic8pdj4KdApGmWF4RUn4E' TWITTER_BOT_ACCESS_TOKEN_SECRET='ctoZbaXCwfF9jO49BfvPNfoTeG1qs0iFwpp9cDnCDTGMm' BARRER_TOKEN='AAAAAAAAAAAAAAAAAAAAAAZubwEAAAAA%2FL6FIXIHMFDrClomRTJ6M7NsoLg%3DKtSSlSWYU3OqHR5XyFTTe8jmGHqLyM5F9BwFXYNq1bilWjQEAS' nohup python guybrush_threepwood_reply_bot.py`


### Production bot:
[@guybrush_quotes](https://twitter.com/guybrush_quotes?s=20&t=uu60Z4Ofq8N_CvZ5crAhfw)


### Resources
- Twitter developper account: https://developer.twitter.com
- Twitter Authentication: https://developer.twitter.com/en/docs/authentication/oauth-2-0/authorization-code
- Twitter Authentication PKCE: https://developer.twitter.com/en/docs/authentication/oauth-2-0/user-access-token
- Twitter authentication PIN-based: https://developer.twitter.com/en/docs/authentication/oauth-1-0a/pin-based-oauth
- Twitter bot project example: https://github.com/twitterdev/FactualCat-Twitter-Bot
- Twitter bot examples in Python: https://realpython.com/twitter-bot-python-tweepy/
- Twitter bot example: https://medium.com/@muhammetbuyuknacar/coding-a-twitter-lyric-mention-bot-with-python-de83b024b9a3
- Python and VSCode: https://code.visualstudio.com/docs/python/python-tutorial
- Python programmer: https://wiki.python.org/moin/BeginnersGuide/Programmers
- os Python: https://docs.python.org/3/library/os.html
- Python scripts on background: https://janakiev.com/blog/python-background/
- Schedule Python: https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e
- Crontab guru: https://crontab.guru/#*_*_*_*_* 
  - Install crontab `crontab my-crontab`
  - Generate crontab with copy `crontab -l > my-crontab`