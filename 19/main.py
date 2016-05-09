#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    toBin = lambda n: "{:#032b}".format(n)[:2:-1]
    p, q, i = map(int, line.strip().split(','))
    p, q = toBin(p), toBin(q)
    print(str(p[i] is q[i]).lower())
