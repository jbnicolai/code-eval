#!/usr/bin/env python3
import fileinput
from math import ceil

for line in fileinput.input():
    low, base = map(int, line.strip().split(','))
    print(base * ceil(low / base))

