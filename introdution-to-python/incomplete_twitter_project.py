import matplotlib.pyplot as pyplot
from sklearn import *
from numpy import ndarray
from numpy import array
from numpy import append
from twitter import *
import tweepy
from tweepy import OAuthHandler

#Twitter API credentials
twitter_api_key = "jS4ZNZKbBPlVUAYTlbZrEx5Lr"
twitter_api_secret = "G98oZVWT22zDMEUZuffU1vyslZQVERFAmMI6JzuGA0kM4FMd7I"
twitter_access_key = "34996225-yp0x65k8rYBqa1l9W6fJzPNBA7kN0127Q6s1ggU5b"
twitter_access_secret = "arBdYztpaUcp2szrYEdC4eKdyyJfaH6lUhQUrMwBXlVyc"

twitter_auth = OAuthHandler(twitter_api_key, twitter_api_secret)
twitter_auth.set_access_token(twitter_access_key, twitter_access_secret)

twitter_api = tweepy.API(twitter_auth)

user = twitter_api.get_user
user_followers = tweepy.Cursor(twitter_api.friends).items()

for follower in tweepy.Cursor(twitter_api.friends).items():
    print(follower.name)