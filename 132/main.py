#!/usr/bin/env python3
import fileinput
from collections import Counter

for line in fileinput.input():
    seq = line.strip().split(',')
    most_common, frequency = Counter(seq).most_common(1)[0]
    print(most_common if frequency > len(seq) // 2 else 'None')

