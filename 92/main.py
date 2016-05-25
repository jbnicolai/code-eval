#!/usr/bin/env python3
import fileinput
import re

for line in fileinput.input():
    print(line.strip().split()[-2])
