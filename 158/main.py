#!/usr/bin/env python3
import fileinput

def bubbleSort(ls, n):
    for pos_upper in range(len(ls) - 1 ,0,-1):
        for i in range(pos_upper):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
        n -= 1
        if n is 0:
            break
    return ls


for line in fileinput.input():
    ls, n = line.strip().split(' | ')
    ls, n = list(map(int, ls.split(' '))), int(n)
    print(' '.join(map(str, bubbleSort(ls, n))))
