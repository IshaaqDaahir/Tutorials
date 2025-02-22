import tweepy

# Twitter API credentials
consumer_key = 'dZxbWYFRCz19cDr1T3VeYiSZq'
consumer_secret = 'HM1nsdKXKZ72odvJsNpfZlnZrC0jRtFDMPIh2953kZeipuLHEf'
access_token = '1114569589671776256-mV7kEug8YAb4wqxmqPLFbltccLVTEQ'
access_token_secret = 'xVfPH3v8E8S7rBTLUK5usbHgCAjn9WIvod5vMRi6AWpIY'

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

while True:
    username = input('Enter Twitter Account: ')
    if len(username) < 1: break
    
    # Fetch User's Timeline
    tweets = api.user_timeline(screen_name=username, count=10)
    
    for tweet in tweets:
        print(tweet.text)   # Print each tweet's text
        # Process other tweet attributes as needed


