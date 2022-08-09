import sys
import math

DEBUG = True

def debug(*kwargs):
    if DEBUG:
        print(*kwargs, file=sys.stderr, flush=True)

def find_x(longA, latA, longB, latB):
    res = (longB - longA) * math.cos((latA + latB)/2)
    return res
    
def find_y(latA, latB):
    res = latB - latA
    return res

def find_dist(x, y):
    res = (math.sqrt((x**2) + (y**2))) * 6371
    return res


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(",","."))
lat = float(input().replace(",","."))

debug("user position:", lon, lat)

result = ""

n = int(input())
for i in range(n):
    defib = input()

    data = defib.split(";")
    # debug(data)

    longB = float(data[4].replace(",","."))
    latB = float(data[5].replace(",","."))

    location = data[1]

    x = find_x(lon, lat, longB, latB)
    y = find_y(lat, latB)
    dist = find_dist(x,y)

    debug(data[0],location, "=> dist:",dist)

    # lowest_dist is not defined in first round, it throws an exception
    try:
        if lowest_dist >= dist :
            lowest_dist = dist
            result = location
    except :
        lowest_dist = dist
        result = location

    debug("lowest_dist:", lowest_dist, result)

print(result)
