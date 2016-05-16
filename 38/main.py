#!/usr/bin/env python3
import fileinput
from itertools import product

for line in fileinput.input():
    n, s = line.strip().split(',')
    n = int(n)
    print(','.join(sorted(list(set(''.join(combination) for combination in (product(*[ s for i in range(n) ])))))))
