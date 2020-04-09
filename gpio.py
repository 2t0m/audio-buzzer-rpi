import configparser
import logging
import os
import sys
import time
from RPi import GPIO

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] buzzer: %(message)s', )

PIN = int(os.getenv('GPIO_PIN'))
SCAN_INTERVAL = float(os.getenv('SCAN_INTERVAL'))
GPIO.setmode(GPIO.BCM)

config = configparser.ConfigParser()
config.sections()

old_power=0

logging.info("Initializing Buzzer on port "+str(PIN)+" with interval of "+str(SCAN_INTERVAL)+"s.")

try:
    while True:
        config.read('/config/conf.buzzer')
        power = config['STATE']['Power']
        localtime = time.asctime( time.localtime(time.time()) )

        if power != old_power:
            if power == '1':
                GPIO.setup(PIN, GPIO.OUT)
                last_buzz = True
                logging.info("Buzzer turned ON")
            else:
                GPIO.setup(PIN, GPIO.IN)
                last_buzz = False
                logging.info("Buzzer turned OFF")

            old_power = power

        elif power == '1':
            if last_buzz == True:
                GPIO.setup(PIN, GPIO.IN)
                last_buzz = False
            else:
                GPIO.setup(PIN, GPIO.OUT)
                last_buzz = True

        time.sleep(SCAN_INTERVAL)
except:
    logging.info(sys.exc_info()[0])
    GPIO.cleanup()
