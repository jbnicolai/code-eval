#!/usr/bin/env python3
import fileinput
import re

regex = re.compile(r'^[^@]+@[^@]+\.[^@]+$')


for line in fileinput.input():
    print('true' if regex.match(line.strip()) else 'false')
