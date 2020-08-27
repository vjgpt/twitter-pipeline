# import tweepy
# from tweepy.auth import OAuthHandler

consumer_key = ''           # Add your API key here
consumer_secret = ''        # Add your API secret key here
access_token = ''           # Add your Access Token key here
access_token_secret = ''    # Add your Access Token secret key here

# Post a tweet
def post_tweets(tweet):
    import tweepy
    from tweepy.auth import OAuthHandler
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    return api.update_status(tweet)
