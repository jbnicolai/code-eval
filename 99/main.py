#!/usr/bin/env python3
import fileinput
import math

for line in fileinput.input():
    line = line.strip().strip('(').strip(')')
    p1, p2 = line.split(') (')
    x1, y1 = p1.split(', ')
    x2, y2 = p2.split(', ')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    print(int(math.hypot(x2 - x1, y2 - y1)))
