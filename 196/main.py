#!/usr/bin/env python3
import fileinput
import re

for line in fileinput.input():
    print(re.sub('(\d)([a-zA-Z]+)(\d)', r'\3\2\1', line.strip()))
