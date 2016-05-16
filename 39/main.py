#!/usr/bin/env python3
import fileinput
from itertools import product

for line in fileinput.input():
    n = int(line)
    seen = set()
    while n is not 1 and not n in seen:
        seen.add(n)
        n = sum([ int(char)**2 for char in str(n) ])
    print(1 if n is 1 else 0)
