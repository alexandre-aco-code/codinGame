import sys
import math

DEBUG = True

def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr, flush=True)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

ascii = []
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ?'

for i in range(h):
    row = input()

    ascii.append(row)

    result = ""

    for c in t:
        
        pos = alphabet.find(c.upper())
        result += [row[i:i+l] for i in range(0, len(row), l)][pos]

    print(result)
