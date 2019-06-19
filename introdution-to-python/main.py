import string
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as panda
import matplotlib.pyplot as pyplot
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import tweepy
import json
from tweepy import OAuthHandler

# Twitter API credentials
twitter_api_key = "jS4ZNZKbBPlVUAYTlbZrEx5Lr"
twitter_api_secret = "G98oZVWT22zDMEUZuffU1vyslZQVERFAmMI6JzuGA0kM4FMd7I"
twitter_access_key = "34996225-yp0x65k8rYBqa1l9W6fJzPNBA7kN0127Q6s1ggU5b"
twitter_access_secret = "arBdYztpaUcp2szrYEdC4eKdyyJfaH6lUhQUrMwBXlVyc"

twitter_auth = OAuthHandler(twitter_api_key, twitter_api_secret)
twitter_auth.set_access_token(twitter_access_key, twitter_access_secret)

twitter_api = tweepy.API(twitter_auth)

tweet_texts = []
tweet_ids = []

tweet_timeline_message = tweepy.Cursor(twitter_api.user_timeline).items(100)

for tweet in tweet_timeline_message:
    text = tweet.text#str(tweet.text.encode("utf-8"))
    id = tweet.id
    tweet_texts.append(text)
    tweet_ids.append(id)

tweet_data_set = {'Id': tweet_ids, 'Text': tweet_texts}
tweet_data_frame = panda.DataFrame(tweet_data_set)

sentimentAnalyzer = SentimentIntensityAnalyzer()

scores = []


print(print("{:-<40} {}".format("I am very happy today", str(score))))

print("USER")
