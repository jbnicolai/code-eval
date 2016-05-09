#!/usr/bin/env python3
import fileinput
import re

for line in fileinput.input():
    needle, haystack = line.strip().split(',')
    print(needle.rfind(haystack))
