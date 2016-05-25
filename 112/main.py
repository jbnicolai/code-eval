#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    ls, swaps = line.strip().split(' : ')
    ls, swaps = ls.split(), [ list(map(int, swap.split('-'))) for swap in swaps.split(', ') ]
    for swap in swaps:
        ls[swap[0]], ls[swap[1]] = ls[swap[1]], ls[swap[0]]
    print(' '.join(ls))
