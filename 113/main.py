#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    l1, l2 = line.strip().split(' | ')
    l1, l2 = l1.split(), l2.split()
    l1, l2 = map(int, l1), map(int, l2)
    print(' '.join(str(x * y) for x, y in zip(l1, l2)))
