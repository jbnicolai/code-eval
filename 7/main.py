#!/usr/bin/env python3
import fileinput
from operator import add, sub, truediv, mul
from collections import deque

operations = { '+': add, '-': sub, '/': truediv, '*': mul }

def parse(tokens):
    token = tokens.popleft()
    return int(token) if token.isdigit() else operations[token](parse(tokens), parse(tokens))

for line in fileinput.input():
    print(parse(deque(line.split())))
