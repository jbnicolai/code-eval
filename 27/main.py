#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    print("{:b}".format(int(line.strip())))