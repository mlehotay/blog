#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import alchemy

AUTHOR = 'Michael Lehotay'
SITENAME = 'mlehotay'
SITEURL = 'https://mlehotay.github.io/blog'

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'

PATH = 'content'
STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
THEME = alchemy.path()

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
