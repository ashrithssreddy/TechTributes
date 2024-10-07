import tweepy
import yaml

# Load credentials from config.yaml
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

twitter_config = config['twitter']

# Twitter API keys
bearer_token = twitter_config['bearer_token']
access_token = twitter_config['access_token']
access_token_secret = twitter_config['access_token_secret']
api_key = twitter_config['api_key']
api_key_secret = twitter_config['api_key_secret']

# Twitter API Authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
client = tweepy.Client(
    bearer_token,
    api_key,
    api_key_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)

def post_tweet(text):
    response = client.create_tweet(text=text)
    return response
