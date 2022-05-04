import tweepy
from tweepy import OAuthHandler

consumer_key = '*'
consumer_secret = '*'
access_token = '*'
access_secret = '*'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,  wait_on_rate_limit=True)

#you'll need to import json to run this script
import csv
import json
import sys
class PrintListener(tweepy.StreamListener):
    def on_data(self, data):
        # Decode the JSON data
        tweet = json.loads(data)

        # Print out the Tweet
        print('@%s: %s' % (tweet['user']['screen_name'], tweet['text'].encode('ascii', 'ignore')))
        with open('StarWarsDay.csv','a') as f:
                f.write(data)


    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    replies=[] 
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)  

# "to:" for screen name (userhandle) e.g. (@jack) without @
# "since_id=" tweet id
#.items(10) is for number retrieved replies (Twitter API limit is 100 per hour
for full_tweets in tweepy.Cursor(api.user_timeline,screen_name='lshyl_',timeout=999999).items(10):
  for tweet in tweepy.Cursor(api.search,q='to:', since_id=1520991154698144587, result_type='recent',timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
      if (tweet.in_reply_to_status_id_str==full_tweets.id_str):
        replies.append(tweet.text)
  print("Tweet :",full_tweets.text.translate(non_bmp_map))
  for elements in replies:

       print("Replies :",elements)

replies.clear()