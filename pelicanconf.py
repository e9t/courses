#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Lucy Park'
AUTHORURL = u'http://dm.snu.ac.kr/~epark'
SITENAME = u'Courses'
SITEURL = ''
REPOURL = 'http://github.com/e9t/courses'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom settings http://docs.getpelican.com/en/3.1.1/settings.html
import os
THEME = 'theme'
FILENAME_METADATA = '(?P<slug>.*)'
USE_FOLDER_AS_CATEGORY = True
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
STATIC_PATHS = [p for p in os.listdir('./%s' % PATH) if not p.startswith('.')]
DEFAULT_PAGINATION = 30     # 30 items in index page

COURSES = ['2015-dm', '2015-ba']

PLUGIN_PATHS = ['plugins']
PLUGINS = ['loadcsv']

GOOGLE_ANALYTICS = 'UA-4510606-3'
#GITHUB_URL = 'http://github.com/e9t/courses'
