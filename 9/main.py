#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    print(' '.join(line.split()[::-2]))
