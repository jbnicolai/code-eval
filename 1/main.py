#!/usr/bin/env python3
import sys

def FB(i, x, y):
    val = 'F' if i % x is 0 else ''
    val += 'B' if i % y is 0 else ''
    return val if val is not '' else str(i)

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        x, y, n = [int(number) for number in test.strip().split(' ')]
        print(' '.join([FB(i, x, y) for i in range(1, n + 1)]))
