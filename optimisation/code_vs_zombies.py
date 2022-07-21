import sys
import math

# Save humans, destroy zombies!


# game loop
while True:
    x, y = [int(i) for i in input().split()] 
    
    humans_x = []
    humans_y = []
    
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
    
    zombies_xnext = []
    zombies_ynext = []
    
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        
        zombies_xnext.append(zombie_xnext)
        zombies_ynext.append(zombie_ynext)

        # zombies = dict.fromkeys(zombie_id,zombie_x)

    # print("zombies", zombies)
    # print(human_x, human_y) #EASY SOLUTION

    # print("zombies_xnext",zombies_xnext)

    dist_x = [c - x for c in zombies_xnext]
    dist_y = [c - y for c in zombies_ynext]

    # zombies = dict.fromkeys(zombies_xnext,zombies_ynext,dist)

    # dist = [(x**2 + y**2)**(1/2) for x,y in zombies_x,zombies_y]
    # dist = (dist_x**2 = dist_y**2)**0.5
 
    
    dist = [ [(dist_x[x]**2 + dist_y[x]**2)**0.5,x] for x in range(len(dist_x))]  
    
    # print(dist)
    # print("min(dist)",min(dist))

    index_closest_zombie = min(dist)[1]

    # print(zombies_xnext[min(dist[1])])






    print(zombies_xnext[index_closest_zombie], zombies_ynext[index_closest_zombie])
