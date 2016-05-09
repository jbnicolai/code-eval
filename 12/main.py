#!/usr/bin/env python3
import fileinput
from collections import Counter

for line in fileinput.input():
    c = Counter(line)
    for char in line:
        if c[char] is 1:
            print(char)
            break
