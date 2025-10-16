import tweepy
import json
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

if __name__ == "__main__":
    try:
        #http object used for interacting with twitter api
        twitterClient = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY,
            access_token=ACCESS_TOKEN,
            wait_on_rate_limit=True,
        )

        # get user id from username
        user = twitterClient.get_user(username="Xiaomi")

        user_id = user.data.id

        # using user id we get tweets
        tweets  = twitterClient.get_users_tweets(
            user_id,
            max_results=50, 
            tweet_fields=['created_at', 'public_metrics', 'text']
        )

        # save the tweets to json file
        with open("extracted_tweets.json", "w") as json_file: #<==== output for analysis of tweets (intermediate output)
            # [].map(e=>e.toString())
            json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
