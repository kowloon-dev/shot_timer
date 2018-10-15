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

# [Shot]
standby_sec = config.get('Shot', 'standby_sec')
shot_count = config.get('Shot', 'shot_count')
shot_interval = config.get('Shot', 'shot_interval')

# [Logging]
logging_level = config.get('Logging', 'logging_level')
log_dir = pardir_path + "/log/"
log_filename = log_dir + config.get('Logging', 'log_filename')

# [Buzzer]
buzzer_pin = config.get('Buzzer', 'buzzer_pin')
buzzer_duration = config.get('Buzzer', 'buzzer_duration')

# [HitCheck]
hit_switch_pin = config.get('HitCheck', 'hit_switch_pin')
hit_deadline = config.get('HitCheck', 'hit_deadline')