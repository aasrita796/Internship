import tweepy
import json

API_KEY = "KM2pdzDGPmc2doLxahhWk3mxT"
API_SECRET_KEY = "4vZJKYIWm3J6IJ3P1XEJZpiIStosATzkau8m3s1PLViJBTADLu"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAALWM3gEAAAAA2q6%2FT%2BwSgOhjjmML7bRltxde3pc%3DCWO1ME0gahzDnL1ZgXEEmkT1L1xjCJeUpUgOgCPoOAD4mUy9l4"
ACCESS_TOKEN = "1668221004878086145-gXubcq1H44vL7e4nJpQvfipJqDP6hS"
ACCESS_TOKEN_SECRET = "mxsgCkZV91nFv9kBDKeFrriybLgMei4lxWzwXdWGiVOcC"



if __name__ == "__main__":
    try:
        twitterClient = tweepy.Client(
            bearer_token=BEARER_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY,
            access_token=ACCESS_TOKEN,
            wait_on_rate_limit=True,
        )

        user = twitterClient.get_user(username="Xiaomi")

        user_id = user.data.id

        # get tweets
        tweets  = twitterClient.get_users_tweets(
            user_id,
            max_results=50, 
            tweet_fields=['created_at', 'public_metrics', 'text']
        )

        # save the tweets to json file
        with open("extracted_tweets.json", "w") as json_file:
            # [].map(e=>e.toString())
            json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")