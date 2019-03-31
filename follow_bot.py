import tweepy
import json
import urllib
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

while True:
    try:
        # Connection Stream to twitter starts here
        class StdOutListener(tweepy.StreamListener):
            ''' Handles data received from the stream. '''
         
            def on_status(self, status):
                if status.user.screen_name != 'crackmeupbro':
                    print '1 ' + status.text
                    tweet ='@' + status.user.screen_name + ' Howdy! Fancy some tickles? @ me and #crackmeup your tweet & get a cool joke! Follow me for cool jokes daily. Keep crackin\'!'
                    print len(tweet)
                    if (len(tweet) <= 140):
                        print '1 ', tweet
                        api.update_status(tweet, status.id, wait_on_rate_limit=True)
                    time.sleep(60*2)
                return True # To continue listening

            def on_error(self, status_code):
                print('1 Got an error with status code: ' + str(status_code))
                return True 
         
            def on_timeout(self):
                print('1 Timeout...')
                return True

        if __name__ == '__main__':
            listener = StdOutListener()
            stream = tweepy.Stream(auth, listener)
            stream.filter(track=['joke', 'jokes', 'comedy', 'funny'])
    except:
        print 'Aww crap'
        time.sleep(60*2)

# Hi there! I'm a joke bot built by @bholagabbar. I tweet jokes daily and tweet jokes back! Try '@crackmeupbro #crackmeup with a blond joke'