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

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError, e:
        return False
    return True

while True:
    try:
        def find_keyword(text):
            text = text.lower()
            if text.find('blond') >= 0 or text.find('blonde') >= 0 :
                return 'blond'
            if text.find('dark') >= 0 :
                return 'dark'
            if text.find('dirty') >= 0 :
                return 'dirty'
            if text.find('men') >= 0 or text.find('women') >= 0 or text.find('boy') >= 0 or text.find('girl') >= 0 or text.find('boys') >= 0 or text.find('girls') >= 0 :
                return 'gender'
            if text.find('gross') >= 0 or text.find('sick') >= 0 :
                return 'gross'
            if text.find('bar') >= 0 or text.find('walks into a bar') >= 0 or text.find('walks into') >= 0 :
                return 'walks-into-a-bar'
            if text.find('yo mama') >= 0 or text.find('mama') >= 0 or text.find('moma') >= 0 or text.find('yomama') >= 0 or text.find('yomoma') >= 0 :
                return 'yo-mama'
            if text.find('chuck norris') >= 0 or text.find('chuck') >= 0 or text.find('norris') >= 0 :
                return 'chuck-norris'
            if text.find('random') >= 0 :
                return 'random'
            else:
                return 'NA'

        def get_joke(tweet):
            if tweet.find('#crackmeup') < 0 :
                return 'Sorry I couldn\'t get that one. Be sure to include #crackmeup in your tweet and tag me!'
            api_keyword = find_keyword(tweet)
            joke = ''
            if api_keyword == 'NA':
                joke = 'Here\'s a random joke! '
                api_keyword = 'random'
            url_to_send = 'http://crackmeup-api.herokuapp.com/' + api_keyword
            print url_to_send
            try:
                joke_json = urllib.urlopen(url_to_send).read()
                joke = json.loads(joke_json)
                joke = joke['joke']
                return joke
            except Exception, e:
                print e
                keepTrying = True
                joke =''
                while keepTrying is True:
                    print 'Trying again'
                    time.sleep(1)
                    joke_json = urllib.urlopen(url_to_send).read()
                    if is_json(joke_json):
                        joke = json.loads(joke_json)
                        if 'joke' in joke:
                            joke = joke['joke']
                            keepTrying = False
                return joke

        def break_tweet(reply, status):
            words = reply.split(' ')
            parts = []
            tw_cnt = 1
            to_add = '@' + str(status.user.screen_name) + ' ' +str(tw_cnt) +'..'
            for word in words:
                if len(to_add + ' ' + word) > 140:
                    dot_cnt = 0
                    while len(to_add) < 140 and dot_cnt < 3:
                        to_add += '.'
                        dot_cnt += 1
                    parts.append(to_add)
                    tw_cnt += 1
                    to_add = '@' + str(status.user.screen_name) + ' ' +str(tw_cnt) +'..' + word + ' '
                else:
                    to_add += word + ' '
            parts.append(to_add)
            if len(parts) == 1:
                parts[0] = parts[0].replace('1..', '')
            return parts

        #Strean Connection to twitter starts here

        class StdOutListener(tweepy.StreamListener):
            ''' Handles data received from the stream. '''
         
            def on_status(self, status):
                print status.text
                joke_text = get_joke(status.text)
                while len(joke_text) > 140:
                    time.sleep(1)
                    joke_text = get_joke(status.text)
                final_tweet = break_tweet(joke_text, status)
                print '3 ' + str(final_tweet)
                for parts in final_tweet:
                    api.update_status(parts, status.id, wait_on_rate_limit=True)
                return True # To continue listening

            def on_error(self, status_code):
                print('3 Got an error with status code: ' + str(status_code))
                return True 
         
            def on_timeout(self):
                print('3 Timeout...')
                return True

        if __name__ == '__main__':
            listener = StdOutListener()
            stream = tweepy.Stream(auth, listener)
            stream.filter(track=['@crackmeupbro'])
    except Exception:
        print '3 awwcrap'
        time.sleep(60)

# Hi there! I'm a joke bot built by @bholagabbar. I tweet jokes daily and tweet jokes back! Try '@crackmeupbro #crackmeup with a blond joke'