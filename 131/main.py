#!/usr/bin/env python3
import fileinput
import re
from operator import add, sub

regex = re.compile('[-+]')

op = { '+': add, '-': sub }

for line in fileinput.input():
    num, patt = line.strip().split()
    search  = regex.search(patt)
    l, r = search.span()
    sign = search.group()
    n1, n2 = num[:int(l)], num[int(l):]
    print(op[sign](int(n1), int(n2)))
