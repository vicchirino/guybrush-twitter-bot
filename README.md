## Twitter Guybrush Threepwood quotes bot.

A simple Twitter bot that tweets a quote every hour of the mighty pirate, Guybrush Threepwood.
Also reply for mentions with a random quote.

### Guybrush quotes

- The secret of Monkey Island: http://www.gamefaqs.com/pc/562681-the-secret-of-monkey-island/faqs/23891
- Lechucks Revenge: https://gamefaqs.gamespot.com/pc/562680-monkey-island-2-lechucks-revenge/faqs/79490
- The curse of Monnkey Island: https://gamefaqs.gamespot.com/pc/29083-the-curse-of-monkey-island/faqs/60819

### Run the bot

1. Clone the project.
2. Create an environment doing `pip install virtualenv` and then `virtualenv {ENVIRONMENT_NAME}`.
3. Activate the virtual if needed `source /{ENVIRONMENT_NAME}/bin/activate` (Note: The method used to activate the virtual environment may be different, depending on your operating system and shell. You can learn more about this in the [venv documentation](https://docs.python.org/3/library/venv.html).)
4. Generate the twitter account keys. Visit https://developer.twitter.com.
5. Run the scrirpt for a single tweet `BOT_USER_ID={BOT_USER_ID} TWITTER_BOT_CONSUMER_KEY='{KEY}' TWITTER_BOT_CONSUMER_SECRET='{KEY}' TWITTER_BOT_ACCESS_TOKEN='{KEY}' TWITTER_BOT_ACCESS_TOKEN_SECRET='{KEY}' python guybrush_threepwood_quotes_bot.py`
6. Run the script for replying mentions `BOT_USER_ID={BOT_USER_ID} TWITTER_BOT_CONSUMER_KEY='{KEY}' TWITTER_BOT_CONSUMER_SECRET='{KEY}' TWITTER_BOT_ACCESS_TOKEN='{KEY}' TWITTER_BOT_ACCESS_TOKEN_SECRET='{KEY}' BARER_TOKEN='{KEY}' nohup python guybrush_threepwood_reply_bot.py`

### Production bot:

[@guybrush_quotes](https://twitter.com/guybrush_quotes?s=20&t=uu60Z4Ofq8N_CvZ5crAhfw)

<img width="691" alt="image" src="https://user-images.githubusercontent.com/3228237/165741417-1028767c-2774-41f9-ad86-964b16874cf2.png">

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
- Crontab guru: https://crontab.guru/#____\*__\__
  - Install crontab `crontab my-crontab`
  - Generate crontab with copy `crontab -l > my-crontab`
  - Access location of crontab files https://www.cyberciti.biz/faq/where-is-the-crontab-file/
