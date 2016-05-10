#!/usr/bin/env python3
import fileinput
import re

regex = re.compile(r'[a-z]+', re.IGNORECASE)

for line in fileinput.input():
    print(' '.join(regex.findall(line)).lower())
