#!/usr/bin/env python3
import fileinput

numwords = {}
units = [
"zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
"nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
"sixteen", "seventeen", "eighteen", "nineteen",
]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

scales = ["hundred", "thousand", "million", "billion", "trillion"]

numwords["and"] = (1, 0)
numwords["negative"] = (1, 0)

for idx, word in enumerate(units):    numwords[word] = (1, idx)
for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

def text2int(words):
    current = result = 0
    sign = -1 if words[0] == "negative" else 1
    for word in words:
        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return sign * (result + current)

for line in fileinput.input():
    print(text2int(line.split()))
