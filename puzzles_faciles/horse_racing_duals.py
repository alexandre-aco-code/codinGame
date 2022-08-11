import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
pui = []
values = set()

for i in range(n):
    pi = int(input())
    pui.append(pi)

pui = sorted(pui)
res = [j-i for i, j in zip(pui[:-1], pui[1:])]

print(min(res))
