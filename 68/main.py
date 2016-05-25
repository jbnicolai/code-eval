#!/usr/bin/env python3
import fileinput

closeToOpen = { '}': '{', ')': '(', ']': '[' }
opens = set(['(', '[', '{'])

for line in fileinput.input():
    stack, balanced = [], True
    for char in line.strip():
        if char in opens:
            stack.append(char)
        else:
            if not stack or closeToOpen[char] is not stack.pop():
                balanced = False
                break

    if stack:
        balanced = False

    print(str(balanced))
