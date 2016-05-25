#!/usr/bin/env python3
import fileinput

primes = [ 3, 7, 31, 127, 2047 ]

for line in fileinput.input():
    n = int(line)
    print(', '.join(str(prime) for prime in primes if prime < n))
