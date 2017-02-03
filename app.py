import flask
import os
import requests
import tweepy
from random import random
from random import randint
from tweepy.models import Status
import json

app = flask.Flask(__name__)

#consumer_key = 	"bgsi3dhSOFgSv7smGbbqviIT9"
#consumer_secret = 	"tqg7y6GjOSzkTV3i0g56XkeORUaVanj7w0OCVSZmz694bzzro9"
#access_token = 	"399817303-XsV9PzDJ83iHtjYWNwjxEiHjOIg7BRI1hkoM2vNl"
#access_token_secret = 	"MsUvIwYuFkuLZZYRZijydLJQeU96bY8wJEuMPdchVRVDq"

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
#api = tweepy.API(auth)
    
@app.route('/')

def index():
    
    #accessing keys
    consumer_key = 	os.getenv("Consumer_key")
    consumer_secret = 	os.getenv("Consumer_secret")
    access_token = 	os.getenv("Access_token")
    access_token_secret = 	os.getenv("Access_secret")
    #getty_key = os.getenv("getty_key")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    
    #getty image
    image_url = randomizeImages()
    
    #twitter
    quoteAPI=randomizeTweets()
    
    #tweet variable
    tweet = quoteAPI.text
    
    #user variable
    user = quoteAPI.user.screen_name
  
    #at_link variable
    tweetID = quoteAPI.id
    tweetIDString = str(tweetID)
    at_link = "twitter.com/" + user + "/status/" + tweetIDString
  
    return flask.render_template("index.html", image_url=image_url, tweet=tweet, user=user, at_link=at_link)
    #config vars key + os.getenv("")
    
    #randomizes tweets    
def randomizeTweets():
    consumer_key = 	os.getenv("Consumer_key")
    consumer_secret = 	os.getenv("Consumer_secret")
    access_token = 	os.getenv("Access_token")
    access_token_secret = 	os.getenv("Access_secret")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    Tweet = api.search("disneyquotes", lang = "en", count = 100)
    randomTweets = sorted(Tweet, key=lambda x: random())
    chosenTweet = randomTweets[0]
    return chosenTweet
    
#randomize images
def randomizeImages():
    #getty_key = os.getenv("getty_key")
    #define header
    my_headers = {'Api-key': 'vvdp68vnrgun32p39z5q8gmg'}
    resolution  = {'fields': 'comp'}
    r = requests.get('https://api.gettyimages.com:443/v3/search/images/editorial?phrase=Disney%20Characters&sort_order=most_popular', headers=my_headers, params=resolution)
    #json data
    images_url = r.json()
    number = randint(0,30)
    image_url = images_url["images"][number]["display_sizes"][0]["uri"]
    return image_url
    
    
app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
)