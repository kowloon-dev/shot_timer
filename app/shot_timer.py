#!/usr/bin/env python3

import wiringpi as pi
from app import buzzer
from app import hit_check
import time
import datetime
from app import config_import as ci
from app import log_control as log

pi.wiringPiSetupGpio()

bz = buzzer.Buzzer()
hc = hit_check.hitCheck()


time.sleep(int(ci.standby_sec))

for i in range (0, int(ci.shot_count)):

    # 確認用
    print(str((i) +1)+ "発目")
    # 開始時刻を計測
    start_time_dt = datetime.datetime.now()
    print("start_time : " + str(start_time_dt))

    # ブザーを鳴らす
    bz.buzzer_beep(ci.buzzer_duration)

    # ヒット判定のループ処理
    # 引数としてタイマーの計測開始時刻を渡す
    result = hc.hit_check(start_time_dt)
    
    print(result)
    
    time.sleep(int(ci.shot_interval))
