#!/usr/bin/env python3
import fileinput

chars = { '00': '1', '0': '0' }

for line in fileinput.input():
    line = line.strip().split()
    pairs = list(zip(line[::2], line[1::2]))
    seqs = [ chars[char] * len(l) for char, l in pairs ]
    n = int(''.join(seqs), 2)
    print(n)
