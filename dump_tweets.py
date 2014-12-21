#!/usr/bin/python3
from twitter import *
from time import sleep
import os
import sys

token = os.environ['twitter_token']
token_key = os.environ['twitter_token_key']
con_secret = os.environ['twitter_con_secret']
con_secret_key = os.environ['twitter_con_secret_key']

t = Twitter( auth=OAuth(token, token_key, con_secret, con_secret_key))

def get_tweets(user,max_id=False):
    if max_id:
        statuses = t.statuses.user_timeline(screen_name=user,include_rts=False,max_id=max_id)
    else:
        statuses = t.statuses.user_timeline(screen_name=user,include_rts=False)
    return {int(s['id_str']):s['text'] for s in statuses}

def print_tweets(h):
    for s in h.values():
       print(s)

if __name__ == '__main__':
    user = sys.argv[1]
    h = {}
    max_id = 0
    while True:
        if h:
            tweets = get_tweets(user,max_id)
        else:
            tweets = get_tweets(user)
        h = dict(list(h.items()) + list(tweets.items()))
        new_max = min(h.keys()) - 1
        if  new_max == max_id:
            break
        else:
            max_id = new_max
            print_tweets(tweets)
        sleep(4)
