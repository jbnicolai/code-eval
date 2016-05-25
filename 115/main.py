#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    nums = [ word for word in line.strip().split(',') if word.isdigit() ]
    words = [ word for word in line.strip().split(',')  if not word.isdigit() ]
    output = []
    if words:
        output.append(','.join(words))
    if nums:
        output.append(','.join(nums))
    print('|'.join(output))
