#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Antonin Jousson'
SITENAME = 'neolin.me'
SITEURL = 'http://neolin.me'

# PATHS
STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = { 'extra/CNAME': {'path': 'CNAME'}}

THEME = "responsive"

MINI_BIO = "Antonin mini bio"
BIO = "Antonin's bio"


PLUGIN_PATHS = ["/Users/Antonin/Documents/Coding stuff/Python/pelican-plugins/"]
PLUGINS = ['neighbors']

PATH = 'content'
OUTPUT_PATH = 'output/'

# Misc
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ( ('Github', 'https://github.com/Antoninj', '&#xe037;'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
