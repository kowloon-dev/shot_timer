#!/usr/bin/env python3

import wiringpi as pi
import time
import log_control as log
import config_import as ci
import traceback
import datetime


class hitCheck:

    def __init__(self):
        try:
            # ヒット検知用スイッチのピン番号をコンフィグから取得
            self.SW_PIN = int(ci.hit_switch_pin)
            pi.pinMode(self.SW_PIN, pi.INPUT)
            pi.pullUpDnControl(self.SW_PIN, pi.PUD_DOWN)
            self.hit_deadline = int(ci.hit_deadline)
        except:
            err = "ヒット検知用スイッチピンの初期設定に失敗.\n"
            log.logging.error(err + traceback.format_exc())
            raise

    def hit_check(self, start_time_dt):

        # 与えられたデッドライン秒数を1000倍する
        # (チェック処理で1000分の1秒刻みでループ処理するため)
        deadline_count = int(self.hit_deadline * 1000)
        for i in range(deadline_count):
            # Switchが通電(HIGH状態を検知)したら、「的に命中した」と判断
            if (pi.digitalRead(self.SW_PIN) == pi.HIGH):
                hit_time_dt = datetime.datetime.now()
                print("hit_time :" + str(hit_time_dt))

                # 所要時間の計算開始
                #
                # 1. 時刻の差分を計算
                #    "的にヒットした時刻" から "ブザーが鳴った時刻(開始時刻)" を減算してデルタ時間を求める
                delta = hit_time_dt - start_time_dt

                # 2. デルタ時間を"秒.マイクロ秒"の形式にする
                result_sec_microsec = str(delta.seconds) + "." + str(delta.microseconds)

                print(result_sec_microsec)

                # 3. 小数点以下2位(100分の1秒単位)より下を切り捨てる
                #    スライスを使い、先頭4桁を取得
                #    この仕様により、10秒を超えるタイムを計測する場合は、
                #    小数点以下は1位までしか取得できない
                result = result_sec_microsec[:4]

                # 命中時の処理終わり
                # forループを抜ける
                break
            else:
                # GPIOピンでHIGHを検知できない = 通電していない = まだ的に命中していない
                # と判断し、1000分の1秒スリープしてからチェックに戻る
                time.sleep(0.001)
        else:
            # 指定した締め切り時間内にヒットを検知しなかった場合の処理:
            # 失敗(的を外した or 締め切り時間内に撃ち込めなかった)と見なし、forループを終える
            print("タイムオーバー！")

            # 戻り値にfailと代入
            result = "FAIL"
            
        return result
