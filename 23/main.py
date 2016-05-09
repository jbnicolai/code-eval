#!/usr/bin/env python3

for i in range(1, 13):
    print(' '.join([ str(i * j).rjust(3) for j in range(1, 13) ]))
