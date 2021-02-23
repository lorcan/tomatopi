#!/usr/bin/python3
import json
from pijuice import PiJuice # Import pijuice module

def getData(response):
    if response['error'] != 'NO_ERROR':
        raise RuntimeError("PiJuice Error: " + response['error']) 
    return response['data']

pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object

data = {}
data.update(getData(pijuice.status.GetStatus()))
data.update(getData(pijuice.status.GetFaultStatus()))
data.update(getData(pijuice.status.GetButtonEvents()))

data.update({'chargeLevel': getData(pijuice.status.GetChargeLevel())})
data.update({'batteryTemperature': getData(pijuice.status.GetBatteryTemperature())})
data.update({'batteryVoltage': getData(pijuice.status.GetBatteryVoltage())})
data.update({'batteryCurrent': getData(pijuice.status.GetBatteryCurrent())})
data.update({'ioVoltage': getData(pijuice.status.GetIoVoltage())})
data.update({'ioCurrent': getData(pijuice.status.GetIoCurrent())})

print(json.dumps(data))
