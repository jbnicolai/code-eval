#!/usr/bin/env python3
import fileinput

m = [ [0] * 256 ] * 256

for line in fileinput.input():
    args = line.strip().split()

    if args[0] == 'SetCol':
        for row in m:
            row[int(args[1])] = int(args[2])

    elif args[0] == 'SetRow':
        m[int(args[1])] = [int(args[2])] * 256

    elif args[0] == 'QueryCol':
        print(sum([ r[int(args[1])] for r in m ]))

    elif args[0] == 'QueryRow':
        print(sum(m[int(args[1])]))

