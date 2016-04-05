#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nicolas L\u0153uillet'
SITENAME = u'a self hostable application for saving web pages'

PATH = 'content'

#WARNING_MESSAGE = u'<strong>2016/04/03: <a href="https://www.wallabag.org/blog/2016/04/03/wallabag-v2">wallabag v2 available! Download it here.</a></strong>'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DISPLAY_PAGES_ON_MENU = True
ARTICLE_URL = '{slug}'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'search')
SITEMAP_SAVE_AS = 'sitemap.xml'

#BANNER = 'images/books.jpg'
#BANNER_ALL_PAGES = False
#BANNER_SUBTITLE = u'Click, save, organize, read it when you want'

DEFAULT_PAGINATION = 6
INDEX_SAVE_AS = 'blog_index.html'
SUMMARY_MAX_LENGTH = None
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'cosmo'
CUSTOM_CSS = 'extra/css/custom.css'
RECENT_POST_COUNT = 3

#BOOTSTRAP_NAVBAR_INVERSE = True
USE_PAGER = True

FAVICON = 'images/favicon.ico'

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = False

MIT_LICENSE = True

HIDE_SITENAME = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

# Revoir la 404 pour insérer quelques liens 

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

STATIC_PATHS = [
    'extra',
    'images',
    'extra/custom.css',
    ]

TEMPLATE_PAGES = {'extra/404.html': '404.html'}

EXTRA_PATH_METADATA = {
    'extra/c89a2a203e9a6045dd4df81b6ca20289.txt': {'path': 'c89a2a203e9a6045dd4df81b6ca20289.txt'},
    'extra/googlef9834aed73023328.html': {'path': 'googlef9834aed73023328.html'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/custom.css': {'path': 'static/custom.css'}
}

READERS = {'html': None}
