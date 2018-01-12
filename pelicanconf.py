#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General info
AUTHOR = 'Antonin Jousson'
HIDE_SITENAME = False
SITENAME = 'Neolin'
SITEURL = 'http://neolin.me'

# About me
AVATAR = 'images/avatar.jpg'
ABOUT_ME = "Hello, I'm antonin."

# Static data paths
STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = { 'extra/CNAME': {'path': 'CNAME'}}

# Theme template 
THEME = "pelican-bootstrap3"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = "paper"

# Menu 
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = ()

# Banner
#BANNER = '/path/to/banner.png'
#BANNER_SUBTITLE = 'This is my subtitle'
#BANNER_ALL_PAGES = True

# Plugins
PLUGIN_PATHS = ["/Users/Antonin/Documents/Coding stuff/Python/pelican-plugins/"]
PLUGINS = ['neighbors','i18n_subsites','related_posts','liquid_tags','tag_cloud']

I18N_TEMPLATES_LANG = 'fr'

# Input and output data paths
PATH = 'content'
OUTPUT_PATH = 'output/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Article info
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True

# Layout
BOOTSTRAP_FLUID = True

# Site Logo
#SITELOGO = 'images/mylogo.jpg'
# SITELOGO_SIZE = 

# Sidebar 
HIDE_SIDEBAR = False
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAGS_URL = "tags.html"

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ( ('github', 'https://github.com/Antoninj', "Github"),
	('linkedin', 'http://www.linkedin.com/in/antonin-jousson-6503b495', "Linkedin")
	)

# Disqus comment
#DISQUS_SITENAME = ''

# Google analytics
#GOOGLE_ANALYTICS = ''

# Misc
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

# Pagination
USE_PAGER = True # bootstrap pagination
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


