import wiringpi as pi
import time

BUZZER_PIN = 23

pi.wiringPiSetupGpio()
pi.pinMode( BUZZER_PIN, pi.OUTPUT )

while True:
    pi.digitalWrite( BUZZER_PIN, pi.HIGH )
    time.sleep(0.3)

    pi.digitalWrite( BUZZER_PIN, pi.LOW )
    time.sleep(4)

exit()

