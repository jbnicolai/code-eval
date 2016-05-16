#!/usr/bin/env python3
import fileinput
from string import ascii_lowercase

alphabet = set(ascii_lowercase)

for line in fileinput.input():
    missing_chars = alphabet.difference(set(line.strip().lower()))
    print(''.join(sorted(list(missing_chars))) if missing_chars else 'NULL')
