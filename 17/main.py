#!/usr/bin/env python3
import fileinput

def mssl(l):
    best = cur = 0
    for i in l:
        cur = max(cur + i, 0)
        best = max(best, cur)
    return best

for line in fileinput.input():
    print(mssl([int(num) for num in line.strip().split(',') ]))

