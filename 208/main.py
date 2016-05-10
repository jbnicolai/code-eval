#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    votes = map(max, zip(*[ map(int, row.split()) for row in line.strip().split(' | ') ]))
    print(' '.join(map(str, votes)))
