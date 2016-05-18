#!/usr/bin/env python3
import fileinput

for line in fileinput.input():
    coords = list(map(int, line.strip().split(',')))
    sq1, sq2 = coords[:4], coords[4:]

    print(sq1[0] > sq2[0] or sq1[2] > sq2[2] or sq1[1] < sq2[1] or sq1[3] < sq2[3] )
