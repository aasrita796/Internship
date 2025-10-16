#DOCUMENTAION

# AI Content Generator

## Overview

This project is an **AI-powered content generator** for Twitter, designed to help tech companies create, analyze, and compare engaging tweets for product launches. It uses the Twitter API to extract real tweets, Google Gemini API for sentiment analysis and tweet generation, and provides a modern web UI for user interaction.

---

## Features

- **Extract Tweets:** Fetches recent tweets from a tech company using Tweepy and Twitter API.
- **Sentiment Analysis:** Analyzes tweets using Gemini API to determine sentiment, engagement, and keywords.
- **Top Tweet Selection:** Selects the top 5 tweets based on engagement score.
- **AI Tweet Generation:** Uses Gemini API to generate two new tweets for a given prompt.
- **Tweet Comparison:** Compares the generated tweets and predicts which will perform better.
- **Web API:** Flask backend exposes endpoints for tweet generation and comparison.
- **Modern UI:** Responsive web interface for entering prompts and viewing results.

---

## Project Structure

```
Internship/
│
├── .env                      # API keys and secrets (not tracked by git)
├── api.py                    # Flask backend API
├── create_tweet.py           # Tweet generation and comparison logic
├── extract_tweets.py         # Extracts tweets from Twitter
├── run_sentiment_analysis.py # Gemini API integration
├── sentiment_analysis.py     # Runs sentiment analysis on tweets
├── extracted_tweets.json     # Raw tweets from Twitter
├── analyzed_tweets.json      # Sentiment-analyzed tweets
├── ui/
│   └── index.html            # Frontend web UI
└── README.md                 # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd Internship
```

### 2. Install Dependencies

```sh
pip install -r requirements.txt
# Or install manually:
pip install tweepy flask flask-cors pandas google-genai
```

### 3. Configure API Keys

- Create a `.env` file in the project root and add your Twitter and Gemini API keys:

```
API_KEY=your_twitter_api_key
API_SECRET_KEY=your_twitter_api_secret
BEARER_TOKEN=your_twitter_bearer_token
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Extract Tweets

Run the extraction script to fetch tweets:

```sh
python extract_tweets.py
```

### 5. Run Sentiment Analysis

Analyze the extracted tweets:

```sh
python sentiment_analysis.py
```

### 6. Start the Flask Backend

```sh
python api.py
```

### 7. Open the Frontend

Open `ui/index.html` in your browser.  
Type your prompt and click "Send" to generate and compare tweets.

---

## Usage

1. **Enter a prompt** (e.g., "Launch the new iPhone 17 Pro Max for camera enthusiasts").
2. **View results:** The app will show Tweet A, Tweet B, a prediction of which is more engaging, and an explanation.
3. **Iterate:** Try different prompts to generate and compare more tweets.

---

## Customization

- **Change the target company:** Edit `extract_tweets.py` to fetch tweets from a different Twitter username.
- **Modify prompt logic:** Update `create_tweet.py` for different product launches or engagement strategies.
- **Style the UI:** Edit `ui/index.html` CSS for a custom look.

---

## Troubleshooting

- **API Quota Errors:** If you hit Gemini or Twitter API limits, wait and retry or upgrade your plan.
- **No Output:** Ensure all scripts run in order and the backend is running before using the frontend.
- **CORS Issues:** Flask-CORS is enabled; if you have issues, check your browser console for errors.

---

## License

MIT License

---

## Credits

- [Tweepy](https://www.tweepy.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Google Gemini API](https://ai.google.dev/)