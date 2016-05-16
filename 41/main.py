#!/usr/bin/env python3
import fileinput
from collections import Counter

for line in fileinput.input():
    _, arr = line.strip().split(';')
    counts = Counter(arr.split(','))
    print(counts.most_common(1)[0][0])
