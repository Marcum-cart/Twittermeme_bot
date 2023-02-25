import tweepy
import time
import datetime
import os
import sys
from genericpath import isfile
import random


#TwitterTokens
all_keys = open('Keys.txt', 'r').read().splitlines()
api_key = all_keys[0]
api_secret_key = all_keys[1]
a_t = all_keys[2]
a_t_s = all_keys[3]
the_bearer_token = all_keys[4]

#Auth to Twitter

client = tweepy.Client(bearer_token=the_bearer_token,
                        consumer_key=api_key,
                        consumer_secret=api_secret_key,
                        access_token=a_t,
                        access_token_secret=a_t_s)

auth = tweepy.OAuthHandler(api_key, api_secret_key, a_t, a_t_s)
api = tweepy.API(auth, wait_on_rate_limit=True)
#"""""
#MEDIA POSTER
## the idea is to have it post a meme/gif once a day or so
# Get the list of all files and directories
path = "/usr/local/Media"
dir_list = []
dir_list = os.listdir(path)
for i in range(1):
    mediaFile = os.path.join(path,random.choice(dir_list))


##post random file pulled from media folder
status = "Hope y'all enjoy today's meme"
api.update_status_with_media(status = status, filename = mediaFile)
#"""

#RETWEET SECTION
##change the hashtags in the search section to specify what to retweet
while True:
    # get time at start of loop
    now = datetime.datetime.now()
    
    for tweet in tweepy.Cursor(api.search_tweets, q=('#drpep OR #drewthoughts -filter:retweets'), lang='en').items(6):
        try:
            # Add \n escape character to print() to organize tweets
            print('\nTweet by: @' + tweet.user.screen_name)
            print('Tweet link: https://twitter.com/' + tweet.user.screen_name + '/status/' + str(tweet.id))

            # Retweet and like tweets as they are found
            tweet.retweet()
            client.like(tweet.id)
            print('---- SUCCESS!')

        except tweepy.errors.TweepyException as e:
            # if tweet is already retweeted/liked, print this.
            print("FAILED - TWEET ALREADY RETWEETED AND LIKED")

        except StopIteration:
            break

    # print time at end of loop
    print ('\n-----     at  ' + str(now.time()) + '     -----')

    # wait for 2 minutes
    time.sleep(120)
    break

print('it worked')