import tweepy
import json
import urllib
import random
import time
import os

#Setup API details
access_token = os.getenv('YOUR_ACCESS_TOKEN')
access_token_secret = os.getenv('YOUR_ACCESS_TOKEN_SECRET')
consumer_key = os.getenv('YOUR_CONSUMER_KEY')
consumer_secret = os.getenv('YOUR_CONSUMER_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# time.sleep(5)

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        return False
    return True

def get_random_tweet():
    topics=['blond', 'dark', 'yo-mama', 'walks-into-bar', 'gender', 'chuck-norris', 'random']
    x = random.choice(topics)
    try:
        url_to_send = 'http://crackmeup-api.herokuapp.com/' + str(x)
        print url_to_send
        joke_json = urllib.urlopen(url_to_send).read()
        joke = json.loads(joke_json)
        joke = joke['joke']
        return joke
    except Exception, e:
        print e
        keepTrying = True
        joke =''
        while keepTrying == True:
            print 'Trying again'
            time.sleep(1)
            joke_json = urllib.urlopen(url_to_send).read()
            if is_json(joke_json):
                joke = json.loads(joke_json)
                if 'joke' in joke:
                    joke = joke['joke']
                    keepTrying = False
        return joke

while True:
    try:
        joke = get_random_tweet()
        while (len(joke + '#crackmeup') > 140):
            joke = get_random_tweet()
        api.update_status(joke + '#crackmeup', wait_on_rate_limit=True)
        print '2 ' + joke
        time.sleep(60*25)
    except Exception, e:
        print str(e) + '2 Oh crap'
        time.sleep(60)
