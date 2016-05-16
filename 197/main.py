#!/usr/bin/env python3
import fileinput
from string import ascii_uppercase

for line in fileinput.input():
    i = int(line)
    c = ''

    while i > 0:
        c = ascii_uppercase[i % 26 - 1] + c
        i = (i - 1) // 26

    print(c)
