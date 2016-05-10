#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    print(int(line.strip(), 16))
