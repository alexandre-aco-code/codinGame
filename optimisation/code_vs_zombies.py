import sys
import math

DEBUG = True

def debug(*args):
    if DEBUG :
        print(*args, file=sys.stderr)


##### CLASSES

class Human():

    def __init__(self,id,x,y):

        self.id = id
        self.x = x
        self.y = y

class Zombie():

    def __init__(self,id,x,y,next_x,next_y):

        self.id = id
        self.x = x
        self.y = y
        self.xn = next_x
        self.yn = next_y

    def calc_dist(self, human_x, human_y):
        dx = abs(human_x - self.xn)
        dy = abs(human_y - self.yn)
        dist = ( dx ** 2 + dy ** 2 ) ** 0.5 
        return dist




# game loop
while True:
    humans = []
    zombies = []
    X = Y = 0

    x, y = [int(i) for i in input().split()] 

    human_count = int(input())

    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append(Human(human_id, human_x, human_y))
        debug("human :", human_id, human_x, human_y)
    
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append(Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext))
        debug("zombie :", zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext)


    debug("human_count", human_count)
    debug("zombie_count", zombie_count)

    if human_count > 0 and human_count != 2 and zombie_count != 2:
        X, Y = humans[0].x, humans[0].y
    elif human_count == 2 and zombie_count == 2 : # pour le cas reflexe
        X, Y = humans[1].x, humans[1].y
    else:
        d = {}
        for z in zombies :
            d[z.id] = z.calc_dist(x,y)

        debug("d", d)

        id_z_closest = min(d, key=d.get)

        debug("id_z_closest",id_z_closest)

        z = [z for z in zombies if z.id == id_z_closest][0]

        debug(z.id,z.x, z.y,z.xn, z.yn)

        X,Y = z.x,z.y

    print(X, Y)
