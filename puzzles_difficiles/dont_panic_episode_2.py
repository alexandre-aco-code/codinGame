import sys

DEBUG = True


################# GET INPUTS ################# 

def get_general_data():
    general_data = [int(i) for i in input().split()]
    return general_data

def get_elevators_data():
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
    return elevators

# change each turn
def get_clones_data():
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT
    return clone_floor, clone_pos, direction

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = get_general_data()

# elevators = dictionnaire qui contient les positions des elevators (values) par niveau (keys)
elevators = get_elevators_data()


################# GENERAL FUNCTIONS ################# 

def debug(*args):
    if DEBUG :
        print(*args, file=sys.stderr)

def get_closest_elevator(elevator_pos,clone_pos,direction):

    #PRENDRE EN COMPTE LA DIRECTION DU CLONE ( DELAI DE 3 SINON )

    distance = width + 1
    closest = 0
    cost = 0 # vaut 0 si la direction du clone est dans le sens de l'elevator, sinon vaut 3

    if len(elevator_pos) >= 2 :
        e_number = 0
        for e in elevator_pos:
            e_number += 1
            # debug("e_number", e_number)

            if (e - clone_pos) > 0 :
                # debug("elevator on the right")
                # debug("direction",direction)
                if direction == "LEFT":
                    cost += 3
            elif (e - clone_pos) < 0:
                # debug("elevator on the left")
                # debug("direction",direction)
                if direction == "RIGHT":
                    cost += 3
            else :
                # debug("on elevator")
                pass

            if distance >= abs(clone_pos - e) + cost:
                distance = abs(clone_pos - e) + cost
                closest = e

            # debug("cost",cost)
            # debug("closest",closest)
            # debug("distance",distance)

    elif len(elevator_pos) == 1 :
        closest = elevator_pos[0]
    
    else:
        closest = None
    
    # debug("closest :", closest)
    return closest

def get_needed_elevators_quantity(elevators,clone_floor):

    needed_elevators_quantity = 0
    floor = 0

    if clone_floor < 0 :
        floor = 0
    else :
        floor = clone_floor

    for f in range(floor, exit_floor):
        elevator_pos = None
        try:
            elevator_pos = elevators[f]
        except:
            elevator_pos = None
        if elevator_pos == None:
            needed_elevators_quantity += 1
    # debug("needed_elevators_quantity",needed_elevators_quantity)
    return needed_elevators_quantity

        







################# CLASSES ################# 

class Game :
    
    def __init__(self) :
        pass

    def run(self):
        clone_floor, clone_pos, direction = get_clones_data()

        elevators[exit_floor] = [exit_pos] #jajoute la sortie aux elevators

        elevators_ordered = dict(sorted(elevators.items(), key=lambda x: x[0]))
        elevator_pos = []
        closest_elevator = -1
        
        needed_elevators_quantity = get_needed_elevators_quantity(elevators_ordered,clone_floor)
        extra_elevators_quantity = nb_additional_elevators - needed_elevators_quantity

        try:
            elevator_pos = elevators[clone_floor]
            closest_elevator = get_closest_elevator(elevator_pos, clone_pos, direction)
        except:
            pass

        # debug("elevators", elevators)
        debug("elevators_ordered", elevators_ordered)
        # debug("nb_additional_elevators",nb_additional_elevators)
        debug("direction :", direction)
        debug("clone_floor :", clone_floor)
        debug("clone_pos :", clone_pos)
        debug("closest_elevator :", closest_elevator)
        # debug("needed_elevators_quantity",needed_elevators_quantity)
        debug("extra_elevators_quantity",extra_elevators_quantity)
        


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

        # 4. On est dans un niveau intermédiaire et pas d'élévator (elevator_pos vide, donc faut en créer un)
        elif not elevator_pos and clone_floor != exit_floor:
            debug("CAS 4. On est dans un niveau intermédiaire et pas d'élévator (faut en créer un)")


            if nb_additional_elevators > 0 :
                print("ELEVATOR")
                

                if clone_floor not in elevators.keys():
                    elevators[clone_floor] = []

                elevators[clone_floor].append(clone_pos)
                # temp = dict(sorted(elevators.items(), key=lambda x: x[0]))
                # debug("temp",temp)
                # elevators = {}
                # elevators = temp

            else : 
                print("WAIT")
                debug("PLUS D ELEVATOR EN STOCK")

        # 5. On est dans un niveau intermédiaire et on va a l'élévator le plus proche (elevator_pos non vide)
        elif bool(elevator_pos) and clone_floor != exit_floor:
            debug("CAS 5. On est dans un niveau intermédiaire et on va a l'élévator le plus proche")


            # si il nous reste des extra elevators on en fait un si c'est loin
            if abs(int(closest_elevator) - clone_pos) > 10:

                #CREATE ELEVATOR
                if extra_elevators_quantity > 0 :
                    print("ELEVATOR")
                    
                    if clone_floor not in elevators.keys():
                        elevators[clone_floor] = []

                    elevators[clone_floor].append(clone_pos)
                    # temp = dict(sorted(elevators.items(), key=lambda x: x[0]))
                    # debug("temp",temp)
                    # elevators = {}
                    # elevators = temp

                else : 
                    print("WAIT")
                    debug("PLUS D ELEVATOR EN STOCK")




            else:

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



################# GAME LOOP ################# 
game = Game()

while True:
    game.run()
