#!/usr/bin/env python3
import fileinput
import itertools

lines = fileinput.input()
desired_nr = int(next(lines))

print('\n'.join(sorted([ line.strip() for line in lines ], key=len, reverse=True)[:desired_nr]))

fileinput.close()
