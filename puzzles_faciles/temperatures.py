import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

closest_t = 500000

temps = []

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    print("t",t, file=sys.stderr, flush=True)

    dif = abs(t-0)
    print("dif",dif, file=sys.stderr, flush=True)

    # result = abs(t-0)

    if dif < abs(closest_t-0) :
        closest_t = t
    # else:
        # result = t

    temps.append(t)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if closest_t < 0 and -closest_t in temps:
    closest_t = -closest_t

if temps != []:
    print(closest_t)
else:
    print("0")
