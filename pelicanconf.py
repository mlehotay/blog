#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import alchemy

AUTHOR = 'Michael Lehotay'
SITENAME = 'mlehotay'
SITESUBTITLE = 'developer blog and assorted data science projects'
SITEURL = 'https://mlehotay.github.io/blog'
ABSOLUTE_URL = SITEURL
DISQUS_SITENAME = "mlehotay"

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'

PATH = 'content'
STATIC_PATHS = ['images', 'attachments']
DELETE_OUTPUT_DIRECTORY = True

DEFAULT_PAGINATION = 10
RELATIVE_URLS = False
THEME = alchemy.path()
