# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    d = ""
    if TY < LY: 
        TY += 1
        d = "S"
    elif TY > LY :
        TY -= 1
        d = "N"
        
    if TX < LX: 
        TX += 1
        d += "E"
    elif TX > LX:
        TX -= 1
        d += "W"

    print(d)
