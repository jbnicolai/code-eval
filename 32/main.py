#!/usr/bin/env python3
import fileinput
import re

for line in fileinput.input():
    needle, haystack = line.strip().split(',')
    print('1' if needle.find(haystack) is not -1 else '0')
