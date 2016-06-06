#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    ns = list(map(int, list("".join(line.strip().split()))))
    total = sum([ 2*x if i % 2 is 0 else x for i, x in enumerate(ns)])
    print('Real' if total % 10 is 0 else 'Fake')
