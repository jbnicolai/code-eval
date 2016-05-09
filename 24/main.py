#!/usr/bin/env python3
import fileinput

print(sum(int(x.strip()) for x in fileinput.input()))
