#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    ls = [ int(x.split('.')[0] + x.split('.')[1]) for x in line.strip().split()]
    print(' '.join([ str(n)[:-3] + '.' + str(n)[-3:] for n in sorted(ls) ]))
