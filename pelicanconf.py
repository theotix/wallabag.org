#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nicolas L\u0153uillet'
SITENAME = u'wallabag'

PATH = 'content'

#WARNING_MESSAGE = u'30/09/2015: <strong>Welcome on our new website!</strong> We are very proud to announce the release of wallabag 2.0. <a href="/blog/2015/09/30/wallabag-v2-alpha-finally" class="alert-link">Please read our blog post</a>.'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DISPLAY_PAGES_ON_MENU = True
ARTICLE_URL = '{slug}'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'search')
SITEMAP_SAVE_AS = 'sitemap.xml'

BANNER = 'images/books.jpg'
BANNER_ALL_PAGES = True
BANNER_SUBTITLE = u'Click, save, organize, read it when you want'

DEFAULT_PAGINATION = 6
INDEX_SAVE_AS = 'blog_index.html'
SUMMARY_MAX_LENGTH = None
THEME = "pelican-bootstrap3"
BOOTSTRAP_THEME = 'simplex'
CUSTOM_CSS = 'extra/css/custom.css'

FAVICON = 'images/favicon.ico'

DISPLAY_CATEGORIES_ON_MENU = False

DISPLAY_TAGS_ON_SIDEBAR = False
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_TAGS_INLINE = True

MIT_LICENSE = True

HIDE_SITENAME = True

DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

WALLABAG_VERSION = "1.9.1"
WALLABAG_DATE_RELEASE = "2015/08/03"

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
