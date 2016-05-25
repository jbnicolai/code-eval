#!/usr/bin/env python3
import fileinput
import re

uppercase = re.compile('[A-Z]')
lowercase = re.compile('[a-z]')

for line in fileinput.input():
    line = line.strip()
    ups = len(uppercase.findall(line))
    lows = len(lowercase.findall(line))
    ratio = int(round(ups / (ups + lows) * 10000)) / 100
    print('lowercase: {0:.2f} uppercase: {0:.2f}'.format(100 - ratio, 2))
