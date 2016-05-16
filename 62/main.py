#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    n, m = map(int, line.strip().split(','))
    print(n - m * (n // m))

