import sys

# CONSTANTS
DEBUG = True
G = 3, 711

# DEBUG
def debug(*args):
    if (DEBUG):
        print(*args, file=sys.stderr, flush=True)

# INPUTS
def collect_land_data():
    land_values = []
    n = int(input())  # le nombre surfaceN de points formant le sol de Mars
    for i in range(n):
        land_x, land_y = [int(j) for j in
                          input().split()]  # couple d'entiers landX landY donnant les coordonnées d’un point du sol
        land_values.append([land_x, land_y])
    return land_values

def collect_capsule_data():
    return [int(i) for i in
            input().split()]  # ligne unique constituée de 7 entiers : X Y hSpeed vSpeed fuel rotate power

# GENERAL METHODS
def find_landing_zone(land_values):
    x1 = x2 = y = 0
    for x in land_values:
        if y == x[1]:
            x2 = x[0]
            break
        x1 = x[0]
        y = x[1]
    return [x1, x2, y]

def get_middle_x_landing_zone(landing_zone):
    mid_x = int((landing_zone[0] + landing_zone[1]) / 2)
    return mid_x

# CODE
landing_zone = find_landing_zone(collect_land_data())

middle_x_landing_zone = get_middle_x_landing_zone(landing_zone)

x1_landing_zone, x2_landing_zone, y_landing_zone = landing_zone

# GAME LOOP
while True:
    # X,Y sont les coordonnées en mètres de la capsule.
    # hSpeed et vSpeed sont respectivement la vitesse horizontale et la vitesse verticale de Mars Lander (en m/s).
    # Suivant le déplacement de Mars Lander, les vitesses peuvent être négatives.
    # fuel est la quantité de fuel restant en litre. Quand le fuel vient à manquer, la puissance des fusées tombe à
    # zéro.
    # rotate est l’angle de rotation de Mars Lander en degré.
    # power est la puissance des fusées de la capsule.
    x, y, hs, vs, f, r, p = collect_capsule_data()

    h = y - y_landing_zone  # hauteur par rapport a la zone d'atterissage

    debug(h)

    P = R = 0

    # La capsule est à gauche de la piste
    if x < x1_landing_zone - 1000:
        # si ca va trop vite
        if hs > 80:
            R = 10
            P = 4
        else:
            R = -45  # tourne vers la droite
            P = 4

    # la capsule est a gauche de la piste mais se rapproche
    elif x < x1_landing_zone and x > x1_landing_zone - 1000:
        if hs < -90:
            R = -90
        elif hs > 90:
            R = 90
        else:
            R = hs
        P = 4

    # La capsule est à droite de la piste
    elif x > x2_landing_zone + 1000:

        # pour le cas HAUT PLATEAU
        if y_landing_zone > 2000:
            R = 0
            P = 4
        else:
            if hs < -80:
                R = -10
                P = 4
            else:
                R = +45  # tourne vers la gauche
                P = 4

    # la capsule est a droite de la piste mais se rapproche
    elif x > x2_landing_zone and x < x2_landing_zone + 1000:
        
        if hs < -90:
            R = -90
        elif hs > 90:
            R = 90
        else:
            R = hs
        P = 3

    # La capsule est sur la piste d'atterissage
    elif x1_landing_zone < x < x2_landing_zone:

        # si on est proche du sol, on redresse le vaisseau on sait jamais
        if h < 300:
            R = 0
            P = 4
        else:
            # perfect case
            if hs < 20 and hs > -20 and vs > -25:
                debug("perfect case")
                R = 0
                P = 3
            else:
                if hs < -90:
                    R = -90
                elif hs > 90:
                    R = 90
                else:
                    R = hs
                P = 4

    # R P. R is the desired rotation angle. P is the desired thrust power.
    print(R, P)
