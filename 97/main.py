#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    heap, keys = line.strip().split('| ')
    keys = list(map(int, keys.split()))
    writer = ''.join(heap[x-1] for x in keys)
    print(writer)
