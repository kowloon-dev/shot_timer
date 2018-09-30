#!/usr/bin/env python3

import wiringpi as pi
import time

class Buzzer:

    def __init__(self):
        try:
            # ブザーを鳴らすためのピン番号を指定
            self.BUZZER_PIN = 23
            pi.pinMode(self.BUZZER_PIN, pi.OUTPUT)
        except:
            err = "ブザー用初期設定に失敗.\n"
            log.logging.error(err + traceback.format_exc())
            raise

    def buzzer_beep(self, seconds):
        
        # ブザーを指定秒数鳴らす(シューターに対する"撃て"の合図)
        pi.digitalWrite(self.BUZZER_PIN, pi.HIGH)
        time.sleep(seconds)

        # ブザーを止める
        pi.digitalWrite(self.BUZZER_PIN, pi.LOW)
        
        return