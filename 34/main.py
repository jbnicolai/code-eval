#!/usr/bin/env python3
import fileinput
from math import sqrt

for line in fileinput.input():
    ls, s = line.strip().split(';')
    ls, s = sorted(map(int, ls.split(','))), int(s)
    i1, i2 = 0, len(ls) - 1
    sums = []
    while i1 < i2:
        added = ls[i1] + ls[i2]
        if added is s:
            sums.append(str(i1) + ',' + str(i2))
            i1 += 1
        elif added < s:
            i1 += 1
        else:
            i2 -= 1

    print(';'.join(sums) if len(sums) > 0 else 'NULL')
