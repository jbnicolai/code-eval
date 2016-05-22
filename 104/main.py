#!/usr/bin/env python3
import fileinput

nums = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


for line in fileinput.input():
    ls = [ str(nums[x]) for x in line.strip().split(';') ]
    print(''.join(ls))
