#!/bin/bash
set -x
cd "$(dirname "$0")";
/usr/bin/python3 pi_juice.py --csv --out ../tmp/pijuice.csv
