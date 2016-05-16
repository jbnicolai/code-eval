#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    print(' '.join([s.capitalize() for s in line.strip().split() ]))
