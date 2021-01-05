#!/usr/bin/python3
import json
from pijuice import PiJuice # Import pijuice module

pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
print(json.dumps(pijuice.status.GetStatus()))
# print(json.dumps(pijuice.status.GetChargeLevel()))
