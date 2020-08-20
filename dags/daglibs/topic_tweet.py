# import tweepy
# from tweepy.auth import OAuthHandler

consumer_key = ''           # Add your API key here
consumer_secret = ''        # Add your API secret key here
access_token = ''           # Add your Access Token key here
access_token_secret = ''    # Add your Access Token secret key here

# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth,wait_on_rate_limit=True,
#     wait_on_rate_limit_notify=True)

def delete_all_tweets():
    import tweepy
    from tweepy.auth import OAuthHandler
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)


    for status in tweepy.Cursor(api.user_timeline).items():
        try:
            api.destroy_status(status.id)
            print ("Deleted:", status.id)
        except:
            print ("Failed to delete:", status.id)

# Post a tweet
def post_tweets(tweet):
    import tweepy
    from tweepy.auth import OAuthHandler
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    return api.update_status(tweet)

# Search for tweets by keyowrd
def search_tweets():
    c=0
    for tweet in api.search(q="Finance", lang="en", rpp=100, count=100, result_type="popular"):
        c+=1
        print(f"{tweet.user.name}:{tweet.text}")
        # print(f"{tweet}")
        # break
    print(c)

# Display tweets on your homepage
def homepage_tweets():   
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(f"{tweet.user.name}:{tweet.text}")
        print (f"Is User verified? {tweet.user.verified}/n")
        print (f"How Many Follower? {tweet.user.followers_count}/n")
        print (f"How many likes? {tweet.favorite_count}/n") 
        print (f"How many Retweets? {tweet.retweet_count}/n")
        print (f"Have you liked it? {tweet.favorited}/n") 
        print (f"Retwweted it? {tweet.retweeted}")
        #print(tweet)