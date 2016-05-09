#!/usr/bin/env python3
import fileinput
import re

for line in fileinput.input():
    a, b = line.strip().split(';')
    a, b = map(int, a.split(',')), map(int, b.split(','))
    intersection = set(a).intersection(b)
    print(','.join(str(x) for x in intersection) if intersection else '\n')
