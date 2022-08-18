import sys
import math

DEBUG = True

def debug(*args):
    if DEBUG :
        print(*args, file=sys.stderr)

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
data = {}
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    data[elevator_floor] = elevator_pos

# on ordonne les infos, niveau par niveau
elevators = dict(sorted(data.items(), key=lambda x: x[0]))


# game loop
while True:
    inputs = input().split()
    clone_floor = int(inputs[0])  # floor of the leading clone
    clone_pos = int(inputs[1])  # position of the leading clone on its floor
    direction = inputs[2]  # direction of the leading clone: LEFT or RIGHT

    debug("elevators", elevators)
    debug("direction :", direction)
    debug("clone_floor :", clone_floor)
    debug("clone_pos :", clone_pos)

    try:
        elevator_pos = elevators[clone_floor]
    except:
        elevator_pos = None

    # si on dépasse sur les bords du terrain
    if clone_pos == width-1 or clone_pos == 0 :
        print("BLOCK")

    else:
        # si je suis au dernier étage
        if elevator_pos == None:
            if clone_pos < exit_pos and direction == "LEFT":
                print("BLOCK")
            elif clone_pos > exit_pos and direction == "RIGHT":
                print("BLOCK")
            else:
                print("WAIT")

        # si je suis dans un étage intérmédiaire
        else:
            debug("elevator_pos existe:",elevator_pos)
            if clone_pos < elevator_pos and direction == "LEFT":
                print("BLOCK")
            elif clone_pos > elevator_pos and direction == "RIGHT":
                print("BLOCK")
            else:
                print("WAIT")
        
