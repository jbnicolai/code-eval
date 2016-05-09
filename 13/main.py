#!/usr/bin/env python3
import fileinput
from collections import Counter

for line in fileinput.input():
    string, rm = line.split(', ')
    print(''.join(char for char in string if char not in rm))
