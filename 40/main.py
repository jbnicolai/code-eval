#!/usr/bin/env python3
import fileinput
from collections import Counter

for line in fileinput.input():
    n = line.strip()
    counts = dict(Counter(n))
    print(all(int(c) is (counts[str(i)] if str(i) in counts else 0) for i, c in enumerate(n)))
