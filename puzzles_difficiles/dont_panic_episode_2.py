import sys
import math

DEBUG = True

def debug(*args):
    if DEBUG :
        print(*args, file=sys.stderr)


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]

# on stocke les infos des elevators dans data comme elles viennent (en vrac)
# data = {}
# elevators = []
# for i in range(nb_elevators):
#     # elevator_floor: floor on which this elevator is found
#     # elevator_pos: position of the elevator on its floor
#     elevator_floor, elevator_pos = [int(j) for j in input().split()]
#     # debug(elevator_floor, elevator_pos )
#     # data[elevator_floor] = elevator_pos

#     elevators.append({
#         "floor": elevator_floor,
#         "pos": elevator_pos,
#     })

# on stocke les infos des elevators dans data comme elles viennent (en vrac)
data = {}
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
        
    if elevator_floor not in data.keys():
        data[elevator_floor] = []

    data[elevator_floor].append(elevator_pos)
    

# on ordonne les infos, niveau par niveau
elevators = dict(sorted(data.items(), key=lambda x: x[0]))

new_floor = False
last_floor = -1

# debug("elevators", elevators)

def find_closest_elevator(elevator_pos):

    distance = width + 1
    closest = 0

    if len(elevator_pos) >= 2 :
        for e in elevator_pos:
            if distance > abs(clone_pos - e):
                distance = abs(clone_pos - e)
                closest = e
                # debug("distance",distance)

    elif len(elevator_pos) == 1 :
        closest = elevator_pos[0]
    
    else:
        closest = 0
    
    debug("closest :", closest)
    return closest


# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT
    elevator_pos = []

    # debug("direction :", direction)
    # debug("clone_floor :", clone_floor)
    # debug("clone_pos :", clone_pos)
    debug("elevators", elevators)
    # debug("last_floor",last_floor)
    # debug("clone_floor",clone_floor)


    if last_floor < clone_floor: #If it's on a new floor, set <new_floor> True
        new_floor = True

    try:
        elevator_pos = elevators[clone_floor]
    except:
        elevator_pos = None

    debug("elevator_pos", elevator_pos)

    if clone_floor >= last_floor:
        last_floor = clone_floor
    else:
        new_floor = False

    debug("new_floor:",new_floor)



    # 1. Le clone est en transition
    if clone_floor == -1 or clone_pos == -1 :
        debug("CAS 1. Le clone est en transition")
        print("WAIT")

    # 2. On touche les bords 
    elif clone_pos == 0 or clone_pos == width - 1 :
        debug("CAS 2. On touche les bords")
        print("BLOCK")

    # 3. On est au dernier étage
    elif clone_floor == exit_floor :
        debug("CAS 3. On est au dernier étage")
        if direction == "LEFT" and clone_pos < exit_pos:
            print("BLOCK")
        elif direction == "RIGHT" and clone_pos > exit_pos:
            print("BLOCK")
        else:
            print("WAIT")

    # 4. On est dans un niveau intermédiaire et pas d'élévator (faut en créer un)
    elif elevator_pos == None and clone_floor != exit_floor:
        debug("CAS 4. On est dans un niveau intermédiaire et pas d'élévator (faut en créer un)")

        if new_floor :

            last_floor = clone_floor
            new_floor = False

            if nb_additional_elevators > 0 :
                print("ELEVATOR")
                elevator = True
            else : 
                print("WAIT")
                debug("PLUS D ELEVATOR EN STOCK")
        
        else:
            print("WAIT")


    # 5. On est dans un niveau intermédiaire et on va a l'élévator le plus proche
    elif elevator_pos != None and clone_floor != exit_floor:
        debug("CAS 5. Tout le reste, basiquement : on a un ou des élévators dans le niveau")

        closest_elevator = find_closest_elevator(elevator_pos)
        debug("closest_elevator :", closest_elevator)


        if direction == "LEFT" and clone_pos < closest_elevator:
            print("BLOCK")
        elif direction == "RIGHT" and clone_pos > closest_elevator:
            print("BLOCK")
        else:
            print("WAIT")
    
    # 6. Tout le reste, on devrait jamais aller la
    else:
        debug("CAS 6. Tout le reste, on devrait jamais aller la")
        print("WAIT")


    # # 5. On crée un elevator      
    # else:



    # # si on dépasse sur les bords du terrain
    # if clone_pos == width - 1 or clone_pos == 0 :
    #     print("BLOCK")

    # else:
    #     # si je suis au dernier étage OU je dois créer un elevator
    #     if elevator_pos != []:
    #         if clone_pos < exit_pos and direction == "LEFT":
    #             print("BLOCK")
    #         elif clone_pos > exit_pos and direction == "RIGHT":
    #             print("BLOCK")
    #         else:
    #             # debug("elevator_pos = None")
    #             # debug("no elevator")
    #             print("WAIT")

    #     # si je suis dans un étage intérmédiaire
    #     else:

    #         closest_pos = 1

    #         min_distance = width + 1
    #         for i in elevator_pos :
    #             if abs(i - clone_pos) < min_distance:
    #                 min_distance = abs(i - clone_pos)
    #                 closest_pos = i
            


    #         debug("closest_pos :",closest_pos)
    #         if clone_pos < closest_pos and direction == "LEFT":
    #             # debug("elevator right:",elevator_pos)
    #             print("BLOCK")
    #         elif clone_pos > closest_pos and direction == "RIGHT":
    #             # debug("elevator left:",elevator_pos)
    #             print("BLOCK")
    #         else:
    #             print("WAIT")
        



    # # objective = {}
    # closest_elevator = None
    # reachable_elevators = [i for i in elevators if i["floor"] == clone_floor]

    
    # if len(reachable_elevators) > 0 :
    #     # on chope l'elevator le plus proche
    #     closest = width+1 
    #     for i in reachable_elevators: 
    #         if abs(clone_pos - i["pos"]) < closest:  
    #             closest = abs(clone_pos - i["pos"])
    #             closest_elevator = i        
            

    # debug("closest_elevator :", closest_elevator)






    # # 1. Le clone est en transition
    # if clone_floor == -1 or clone_pos == -1 :
    #     debug("CAS 1. Le clone est en transition")
    #     print("WAIT")

    # # 2. On touche les bords
    # elif clone_pos == 0 or clone_pos == width - 1 :
    #     debug("CAS 2. On touche les bords")
    #     print("BLOCK")

    # # 3. On est au dernier étage
    # elif clone_floor == exit_floor :
    #     debug("CAS 3. On est au dernier étage")
    #     if direction == "LEFT" and clone_pos < exit_pos:
    #         print("BLOCK")
    #     elif direction == "RIGHT" and clone_pos > exit_pos:
    #         print("BLOCK")
    #     else:
    #         print("WAIT")

    # # 4. On a un elevator proche
    # elif closest_elevator != None:
    #     debug("CAS 4. On a un elevator proche")
    #     if direction == "LEFT" and clone_pos < closest_elevator["pos"]:
    #         print("BLOCK")
    #     elif direction == "RIGHT" and clone_pos > closest_elevator["pos"]:
    #         print("BLOCK")
    #     else:
    #         print("WAIT")

    # # 5. On crée un elevator      
    # else:
    #     debug("CAS 5. On crée un elevator")

    #     if nb_additional_elevators > 0 :
    #         print("ELEVATOR")
    #     else : 
    #         debug("PLUS D ELEVATOR EN STOCK")