#!/usr/bin/env python3
import fileinput
import re

regex = re.compile(r'(.+?)(\s\1)+$')

for line in fileinput.input():
    print(regex.search(line.strip()).group(1))

fileinput.close()
