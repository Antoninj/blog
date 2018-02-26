#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# General info
AUTHOR = 'Antonin Jousson'
SITELOGO ='images/logo.png'
SITELOGO_SIZE = 45
HIDE_SITENAME = False
SITENAME = 'Neolin'
SITEURL = 'http://neolin.me'

# About me
AVATAR = 'images/avatar.png'
ABOUT_ME = "Hello, I'm antonin."

# Static data paths
STATIC_PATHS = ['images', 'pdfs', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Theme template
THEME = "/Users/Antonin/Documents/Coding stuff/python/neolin.me/pelican-bootstrap3"
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = "paper"

# Menu
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = ()

# Banner
BANNER = 'images/banner_nc.jpg'
# BANNER_TITLE = ''
# BANNER_SUBTITLE = ''
BANNER_ALL_PAGES = True


# Article list
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Plugins
PLUGIN_PATHS = ["/Users/Antonin/Documents/Coding stuff/python/pelican/pelican-plugins/"]
PLUGINS = ['neighbors', 'i18n_subsites', 'related_posts', 'liquid_tags', 'tag_cloud']

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

# Layout
BOOTSTRAP_FLUID = True

# Site Logo
# SITELOGO = 'images/mylogo.jpg'
# SITELOGO_SIZE =

# Sidebar
HIDE_SIDEBAR = False
SIDEBAR_ON_LEFT = True
BOOTSTRAP_NAVBAR_INVERSE = True

DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
TAGS_URL = "tags.html"

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/Antoninj', "Github"),
          ('linkedin',
           'http://www.linkedin.com/in/antonin-jousson-6503b495',
           "Linkedin"))

# Disqus comment
DISQUS_SITENAME = 'neolin-me'

# Google analytics
# GOOGLE_ANALYTICS = ''

# Misc
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'

# Pagination
USE_PAGER = True   # bootstrap pagination
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
