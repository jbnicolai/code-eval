#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    n, *ls = line.split()[::-1]
    n, l = int(n) - 1, len(ls)
    if n < l:
        print(ls[n])
