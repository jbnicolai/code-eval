#!/usr/bin/env python3
import fileinput
from collections import Counter

for line in fileinput.input():
    ls = list(map(int, line.strip().split()))
    uniques = [ x for x, y in Counter(ls).most_common() if y == 1 ]
    print((ls.index(min(uniques)) + 1) if uniques else 0)
