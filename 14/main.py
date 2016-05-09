#!/usr/bin/env python3
import fileinput
from itertools import permutations

for line in fileinput.input():
    print(','.join(sorted(''.join(perm) for perm in permutations(line.strip()))))
