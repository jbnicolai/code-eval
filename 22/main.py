#!/usr/bin/env python3
import fileinput

class Memoize:
 def __init__(self, fn):
  self.fn = fn
  self.memo = {}
 def __call__(self, arg):
  if arg not in self.memo:
   self.memo[arg] = self.fn(arg)
   return self.memo[arg]

@Memoize
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a

for line in fileinput.input():
    print(fib(int(line.strip())))
