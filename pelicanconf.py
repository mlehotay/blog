#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import alchemy

AUTHOR = 'Michael Lehotay'
SITENAME = 'mlehotay'
SITESUBTITLE = 'blog'
SITEURL = 'https://mlehotay.github.io/blog'

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'

PATH = 'content'
STATIC_PATHS = ['images']

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
THEME = alchemy.path()
