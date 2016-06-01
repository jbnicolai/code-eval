#!/usr/bin/env python3
import fileinput
from itertools import combinations, chain

for line in fileinput.input():
    numbers = list(map(int, line.strip().split(',')))
    combs = list(chain.from_iterable(combinations(numbers, i) for i in range(1, 5)))
    print(combs)
    print([c for c in combs if sum(c) is 0])
