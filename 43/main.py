#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    arr = list(map(int, line.split()))
    if len(arr) is 1:
        print('Jolly')
    else:
        print('Jolly' if set([ abs(arr[i] - arr[i-1]) for i in range(1, len(arr)) ]) == set(range(1, len(arr) - 1)) else 'Not jolly')


