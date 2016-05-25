#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    print(' '.join([s[0].upper() + s[1:] for s in line.strip().split() ]))
