import os

from dotenv import load_dotenv
import tweepy as tw
import pandas as pd
import datetime

def load_tweets_from_twitter(noOfTweet = 200):
    ###### Importing API credentials from the environment 
    
    load_dotenv()

    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')
    access_token = os.getenv('access_token')
    access_token_secret = os.getenv('access_token_secret')

    #####   Establishing connection with the API

    auth = tw.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    # Search parameter for the API 

    search_words = "#hashtag til:2023-02-02"
    


    # Getting results from the API

    tweets = tw.Cursor(api.search_tweets,
                q=search_words,
                tweet_mode = "extended").items(noOfTweet)

    tweets = [[tweet.id,tweet.full_text,tweet.created_at,tweet.user.location,] for tweet in tweets]
    tweets_df = pd.DataFrame(tweets,columns = ['id', 'tweet','creation_date','location'])
    tweets_df.to_csv('tweets.csv',index="id")
    tweets_df.head()



load_tweets_from_twitter()