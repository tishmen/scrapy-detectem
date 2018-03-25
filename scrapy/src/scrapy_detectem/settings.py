'''settings.py'''

import os


# Scrapy settings

BOT_NAME = 'scrapy_detectem'
SPIDER_MODULES = ['scrapy_detectem']


# Custom settings

DETECTEM_URL = os.getenv('DETECTEM_URL')
