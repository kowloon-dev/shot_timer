#!/usr/bin/env python3

import wiringpi as pi
import buzzer
import time
import datetime
import config_import as ci
import log_control as log


pi.wiringPiSetupGpio()


time.sleep(5)

# 開始時刻を計測
start_time_dt = datetime.datetime.now()
print("start_time : " + str(start_time_dt))