#!/usr/bin/env python3
#
# Read CSV files and output their contents as JSON Lines.

import csv, json, sys

for arg in sys.argv[1:]:
    with open(arg) as file:
        for record in csv.DictReader(file):
            print(json.dumps(record))
