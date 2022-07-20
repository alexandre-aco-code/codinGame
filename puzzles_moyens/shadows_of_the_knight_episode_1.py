import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x = x0
y = y0

x_min = 0
y_min = 0

x_max = w
y_max = h



while True:
    bomb_dir = input()  # the direction of the bombs

    #if "R" in bomb_dir:
    #   print("test")

    if "R" in bomb_dir:
        x_min = x

    elif "L" in bomb_dir:
        x_max = x

    if "D" in bomb_dir:
        y_min = y 

    elif "U" in bomb_dir:
        y_max = y 

    x = (x_min + x_max)//2
    y = (y_min + y_max)//2


    print(x,y)
    #print(0,0)

print("Debug messages...", file=sys.stderr, flush=True)
