#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import alchemy

AUTHOR = 'Michael Lehotay'
SITENAME = 'mlehotay'
SITESUBTITLE = 'developer blog and motley assemblage of data science projects'
SITEURL = 'https://mlehotay.github.io/blog'
GOOGLE_ANALYTICS = "UA-158784371-3"
DISQUS_SITENAME = "mlehotay"

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = 'en'

PATH = 'content'
STATIC_PATHS = ['images', 'attachments']
DELETE_OUTPUT_DIRECTORY = True

DEFAULT_PAGINATION = 10
RELATIVE_URLS = True
THEME = alchemy.path()
