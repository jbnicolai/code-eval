#!/usr/bin/env python3
import fileinput
import re

regex = re.compile('(<--<<|>>-->)')

for line in fileinput.input():
    print(line.strip())
    print(regex.findall(line), overlapped=True)
