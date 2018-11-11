#!/usr/bin/env python3

import wiringpi as pi
import buzzer
import hit_check
import result_convert
import time
import datetime
import config_import as ci
import log_control as log

pi.wiringPiSetupGpio()

bz = buzzer.Buzzer()
hc = hit_check.hitCheck()
rc = result_convert.ResultConvert()


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
    
    # 2018/11/11 Add ここから
    # 結果をテンプレートHTMLに出力する処理
    result_html = rc.convert(result)
    # 2018/11/11 Add ここまで
    
    
    time.sleep(int(ci.shot_interval))

# トレーニング終了を知らせる合図
# 1秒のブザーを鳴らす
bz.buzzer_beep(1)
