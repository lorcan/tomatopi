#!/usr/bin/python3
# This script is started at reboot by cron
# Since the start is very early in the boot sequence we wait for the i2c-1 device

import pijuice, time, os, logging
logging.basicConfig(
    filename='/home/lorcan/src/tomatopi/log/wakeup.log', 
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

logging.info('Running wakeup_enable script')

while not os.path.exists('/dev/i2c-1'):
    logging.info('Waiting for i2c-1 device')
    time.sleep(0.1)

pj = pijuice.PiJuice(1, 0x14)

logging.info('Setting wakeup enabled')
pj.rtcAlarm.SetWakeupEnabled(True)
status = pj.rtcAlarm.GetControlStatus()['data']['alarm_wakeup_enabled']
logging.info('Wakeup enabled set: %s', status)
