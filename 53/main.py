#!/usr/bin/env python3
import fileinput
import re

regex = re.compile(r'([^ ]+).*\1')

for line in fileinput.input():
    matches = regex.findall(line)
    print(max(matches, key=len) if matches else 'NONE')
