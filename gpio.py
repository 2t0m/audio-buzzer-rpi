import time
from RPi import GPIO
import configparser

PIN = 4
GPIO.setmode(GPIO.BCM)

config = configparser.ConfigParser()
config.sections()

old_power=0

try:
    while True:
        config.read('/config/conf.buzzer')
        power = config['STATE']['Power']
        localtime = time.asctime( time.localtime(time.time()) )

        if power != old_power:
            if power == '1':
                GPIO.setup(PIN, GPIO.OUT)
                last_buzz = True
                print(localtime + " Buzzer turned ON")
            else:
                GPIO.setup(PIN, GPIO.IN)
                last_buzz = False
                print(localtime + " Buzzer turned OFF")

            old_power = power

        elif power == '1':
            if last_buzz == True:
                GPIO.setup(PIN, GPIO.IN)
                last_buzz = False
            else:
                GPIO.setup(PIN, GPIO.OUT)
                last_buzz = True

        time.sleep(0.3)
except:
    GPIO.cleanup()
