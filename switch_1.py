#!/usr/bin/env python3

import wiringpi as pi
import time

SW_PIN = 4

pi.wiringPiSetupGpio()
pi.pinMode( SW_PIN, pi.INPUT )
pi.pullUpDnControl( SW_PIN, pi.PUD_DOWN )

while True:
    if ( pi.digitalRead( SW_PIN ) == pi.HIGH ):
        print("Switch is On")
        # 通電を検知したら、ループを抜ける
        break
    else:
        print("Switch is Off")
