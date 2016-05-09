#!/usr/bin/env python3
import fileinput
import re

for line in fileinput.input():
    print(','.join(map(str, list(set(map(int, line.strip().split(',')))))))
