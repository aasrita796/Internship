import pandas as pd
import json

from run_sentiment_analysis import execute_gemini_for_tweet_creation

def top_5_selection(analysed_tweets, engagement_type:str):
    tweet_dicts = [json.loads(tweet) for tweet in analysed_tweets]
    df = pd.DataFrame(tweet_dicts)
    filtered_df = df[df['engagement_type'] == engagement_type]  # Filter rows based on engagement_type
    print("DataFrame columns:", df.columns)  # Add this line to debug
    return filtered_df.nlargest(5, columns=['engagement_score']).values.tolist() # Select top 5 rows based on engagement_score

def create_tweet(analysed_tweets):
    prompt = """
    write a tweet for newly releasing iphone 17 pro max with a 18 pro lauching with physically moving camera zoom, make this tweet more for camera enthuisiasts, make it engaging and exciting, use hashtags and emojis, keep it under 280 characters"""
    engagement_type = "like"

    top_5_tweets = top_5_selection(analysed_tweets, engagement_type)
    print(len(top_5_tweets))

    system_prompt = f"""
    Create a engaging twitter tweet for my tech company 
    PROMPT: {prompt}

    Here are some example tweets and their sentiment analysis with vry high user engagements of other similar companies. Example tweets : {top_5_tweets}

    Create the tweet compare it with the example tweets and predict and explain why and how this tweet will perform well comparing to the given examples."""

    out = execute_gemini_for_tweet_creation(
    prompt=system_prompt,
    )

    out_dict = json.loads(out)
    tweet = out_dict["tweet"]
    prediction = out_dict["prediction"]
    explanation = out_dict["explanation"]

    print("Generated Tweet: ", tweet)
    print("Prediction: ", prediction)
    print("Explanation: ", explanation)

with open("analyzed_tweets.json") as f:
    data = json.load(f)
    print("tweets loaded",data)
    create_tweet(data)