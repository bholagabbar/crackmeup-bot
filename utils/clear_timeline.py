import tweepy

# Authentication details. To  obtain these visit dev.twitter.com
access_token = {YOUR_ACCESS_TOKEN}
access_token_secret = {YOUR_ACCESS_TOKEN_SECRET}
consumer_key = {YOUR_CONSUMER_KEY}
consumer_secret = {YOUR_CONSUMER_SECRET}

if __name__ == '__main__':
    # Create authentication token
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Getting all tweets..."

    # Get all tweets for the account
    # API is limited to 350 requests/hour per token
    # so for testing purposes we do 10 at a time
    api = tweepy.API(auth)
    timeline = api.user_timeline(count = 200)

    print "Found: %d" % (len(timeline))
    print "Removing..."
    print "Check https://twitter.com/c4107142 to see the result"

    # Delete tweets one by one
    for t in timeline:
        api.destroy_status(t.id)

    print "Twitter timeline removed!"