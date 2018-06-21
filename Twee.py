from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import tweepy

arr = []

#Variables that contains the user credentials to access Twitter API 
access_token = "Your-Access-Token"
access_token_secret = "Your-Access-Token-Secret"
consumer_key = "Your-Consumer-Key"
consumer_secret = "Your-Consumer-Secret"

login = tweepy.OAuthHandler(consumer_key, consumer_secret)
login.set_access_token(access_token, access_token_secret)
api = tweepy.API(login)

for tweet in tweepy.Cursor(api.search,
                           q="secim AND hile",
                           # Since="2016-08-09",
                           # until="2014-02-15",
                           lang="tr",
                           tweet_mode="extended").items(5000000):

    if 'RT @' not in tweet.full_text:
        with open("data.txt", "a", encoding="UTF-8") as f:
            print(tweet.full_text)
            f.writelines((" ".join(str(x) for x in tweet.full_text.replace('\n', '.').replace('.', ' ').split(" ")[:-1]))+"\n")
