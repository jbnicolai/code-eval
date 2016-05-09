#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    print(sum(int(char) for char in "{0:b}".format(int(line))))

