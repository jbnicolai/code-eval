#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    words, indexes = line.strip().split(';')
    pairs = list(zip(indexes.split(), words.split()))
    ordered = sorted(pairs, key=lambda tup: int(tup[0]))
    print(' '.join([ word for i, word in ordered ]))


