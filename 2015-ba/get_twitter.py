#! /usr/bin/python3
# -*- coding: utf-8 -*-

import csv
from twython import Twython

import settings as s

twitter = Twython(s.APP_KEY, s.APP_SECRET, s.OAUTH_TOKEN, s.OAUTH_TOKEN_SECRET)
tweets = twitter.search(q='삼성', count=100)

data = [(t['user']['screen_name'], t['text'], t['created_at']) for t in tweets['statuses']]

with open('tweets.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)
