#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import pardir
from os.path import dirname
from os.path import sep
import configparser
import logging
import traceback

# Construct config_file path & read config file
try:
    pardir_path = dirname(__file__) + sep + pardir
    config_file = pardir_path + "/config/config.ini"
    config = configparser.ConfigParser()
    config.read(config_file)
except:
    logging.error(traceback.format_exc())
    raise

# ------------  Import parameters from config file  ------------

# [Global]
notify_method = config.get('Global', 'notify_method')

# [GetWebsite]
item_url =             config.get('GetWebsite', 'item_url')
tag_name =       config.get('GetWebsite', 'tag_name')
tag_class =     config.get('GetWebsite', 'tag_class')
keyword =           config.get('GetWebsite', 'keyword')
retry_sleep_min = int(config.get('GetWebsite', 'retry_sleep_min'))
retry_sleep_max = int(config.get('GetWebsite', 'retry_sleep_max'))
retry_max =       int(config.get('GetWebsite', 'retry_max'))
