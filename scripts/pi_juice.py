#!/usr/bin/python3
import argparse
import json
from pijuice import PiJuice # Import pijuice module
import csv, sys
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--csv", action="store_true", help="output in csv format")
parser.add_argument("--out", default='.', help="the directory where we will save the data")
args = parser.parse_args()

def getData(response):
    if response['error'] != 'NO_ERROR':
        raise RuntimeError("PiJuice Error: " + response['error']) 
    return response['data']

pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object

data = {'time': str(datetime.now())}
data.update(getData(pijuice.status.GetStatus()))
data.update(getData(pijuice.status.GetFaultStatus()))
data.update(getData(pijuice.status.GetButtonEvents()))

data.update({'chargeLevel': getData(pijuice.status.GetChargeLevel())})
data.update({'batteryTemperature': getData(pijuice.status.GetBatteryTemperature())})
data.update({'batteryVoltage': getData(pijuice.status.GetBatteryVoltage())})
data.update({'batteryCurrent': getData(pijuice.status.GetBatteryCurrent())})
data.update({'ioVoltage': getData(pijuice.status.GetIoVoltage())})
data.update({'ioCurrent': getData(pijuice.status.GetIoCurrent())})

if args.csv:
    filename = args.out
    with open(filename, 'a+', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data.values())
else:
    print(json.dumps(data))
