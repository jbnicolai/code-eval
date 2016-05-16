#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    l = line.strip()
    power = len(l)
    print(sum([ int(c)**power for c in l ]) == int(l))

