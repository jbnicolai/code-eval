#!/usr/bin/env python3
import fileinput
from math import sqrt

for line in fileinput.input():
    i = int(line.strip())
    count = 0
    valuesArr = []
    for x in range(int(sqrt(i))+1):
        y = sqrt(i - x*x)
        if y == int(y):
            if x*x == y:
                count += 2
            else:
                count += 1
    print(str(count//2))

