#!/usr/bin/env python3
import fileinput
import re

for line in fileinput.input():
    print()
    print(re.sub('(.)\1+', r'----', line.strip()))
