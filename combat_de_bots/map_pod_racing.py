import sys
import math

# CONSTANTS
DEBUG = True
CHECKPOINT_RADIUS = 600  # The radius of a checkpoint
DIST_SLOWDOWN = 1500  # At what distance from checkpoint we slow down
DIST_BOOST = 5000  # At what distance from checkpoint is it safe to boost
ANGLE_MAX_SPEED = 20 # angle to max thurst
ANGLE_BOOST = 2  # At what angle from checkpoint is it safe to boost
THRUST_MIN = 0  # Thrust when we are going in the wrong direction
THRUST_MAX = 100

# DEBUG
def debug(*args):
    if DEBUG:
        print(*args, file=sys.stderr)


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

laps = int(input())
checkpoint_count = int(input())
checkpoints = []
for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoints.append([checkpoint_x,checkpoint_y])




# CLASS
class Pod :

    def __init__(self,x, y, vx, vy, angle, next_check_point_id):

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.angle = angle
        self.next_check_point_id = next_check_point_id
        self.px = x
        self.py = y

    def set_x(self, val):
        self.px = self.x
        self.x = val

    def set_y(self, val):
        self.py = self.y
        self.y = val

    def set_vx(self,val):
        self.vx = val

    def set_vy(self,val):
        self.vy = val

    def set_angle(self,val):
        self.angle = val

    def set_next_check_point_id(self, val):
        self.next_check_point_id = val


    @property
    def next_cp(self):
        return checkpoints[self.next_check_point_id]

    @property
    def d(self):
        check_x, check_y = self.next_cp
        X = check_x - self.x
        Y = check_y - self.y
        d = int(math.sqrt(X**2 + Y**2))
        # debug("dist_to_checkpoint:", d)
        return d

    @property
    def steering(self):
        vx = self.x - self.px
        vy = self.y - self.py

        # debug("vx, vy", vx, vy)

        check_x, check_y = self.next_cp
        # debug("next cp", check_x, check_y)
        
        steering_x = check_x - 2 * vx
        steering_y = check_y - 2 * vy
        
        return steering_x, steering_y

    @property
    def relative_angle(self):

        x,y = self.x, self.y
        a = self.angle
        cx,cy = self.next_cp

        debug("x,y,a,cx,cy", x,y,a,cx,cy)  

        a_abs_cp = - math.degrees(math.atan(cy-y/cx-x))

        debug("a_abs_cp", a_abs_cp)

        rel_a = a_abs_cp - a

        debug("rel_a", rel_a)






## FAIRE UNE CALSSE RACER, ET UNE CLASSE FIGHTER QUI HERITENT DE POD

class Racer(Pod) :

    def __init__(self,x, y, vx, vy, angle, next_check_point_id):

        Pod.__init__(self,x, y, vx, vy, angle, next_check_point_id)


class Fighter(Pod):

    def __init__(self,x, y, vx, vy, angle, next_check_point_id):

        Pod.__init__(self,x, y, vx, vy, angle, next_check_point_id)
        






my_pods = []
oppo_pods = []

class Game:
    
    def __init__(self):

        self.boost = 1
        self.turn = 0 

    def run(self):

        self.turn = self.turn + 1
        debug("turn :", self.turn)

        for i in range(2):
            # x: x position of your pod
            # y: y position of your pod
            # vx: x speed of your pod
            # vy: y speed of your pod
            # angle: angle of your pod
            # next_check_point_id: next check point id of your pod
            x, y, vx, vy, angle, next_check_point_id = [int(j) for j in input().split()]

            if i == 0 :
                debug("racer :",x, y, vx, vy, angle, next_check_point_id)
                pass
            if i == 1 :
                # debug("fighter :",x, y, vx, vy, angle, next_check_point_id)
                pass

            try:
                # debug("update values pods")
                my_pods[i].set_x(x)
                my_pods[i].set_y(y)
                my_pods[i].set_vx(vx)
                my_pods[i].set_vy(vy)
                my_pods[i].set_angle(angle)
                my_pods[i].set_next_check_point_id(next_check_point_id)
            except:
                if i == 0 :
                    my_pods.append(Racer(x, y, vx, vy, angle, next_check_point_id))
                elif i == 1 :
                    my_pods.append(Fighter(x, y, vx, vy, angle, next_check_point_id))
                else : # in case there are more than 2 Pods in the future
                    my_pods.append(Pod(x, y, vx, vy, angle, next_check_point_id))

        for i in range(2):
            # x_2: x position of the opponent's pod
            # y_2: y position of the opponent's pod
            # vx_2: x speed of the opponent's pod
            # vy_2: y speed of the opponent's pod
            # angle_2: angle of the opponent's pod
            # next_check_point_id_2: next check point id of the opponent's pod
            x_2, y_2, vx_2, vy_2, angle_2, next_check_point_id_2 = [int(j) for j in input().split()]
            
            try:
                # debug("update values pods")
                oppo_pods[i].set_x(x_2)
                oppo_pods[i].set_y(y_2)
                oppo_pods[i].set_vx(vx_2)
                oppo_pods[i].set_vy(vy_2)
                oppo_pods[i].set_angle(angle_2)
                oppo_pods[i].set_next_check_point_id(next_check_point_id_2)
            except:
                oppo_pods.append(Pod(x_2, y_2, vx_2, vy_2, angle_2, next_check_point_id_2))


        racer, fighter = my_pods

        X1, Y1 = racer.steering
        X2, Y2 = fighter.steering

        thurst = 100

        debug("racer.d", racer.d)
        debug("relative_angle", racer.relative_angle)

        print(X1, Y1, thurst)
        print(X2, Y2, thurst)



        # # checkpoint est derrière
        # if abs(a) > 90:
        #     thurst = THRUST_MIN

        # # checkpoint est un peu sur le coté
        # elif ANGLE_MAX_SPEED <= abs(a) <= 90 :

        #     # (1 - angle/90) clamped in [0,1]: the more misaligned we are, the more we slow down.
        #     slowdown_for_rotation = 1 - abs(a/90)
        
        #     # debug("slowdown_for_rotation",slowdown_for_rotation)
        #     thurst = int(THRUST_MAX * slowdown_for_rotation)

        # # Checkpoint est devant => A fond! Et on essaie de booster
        # elif abs(a) <= ANGLE_MAX_SPEED :
            
        #     if abs(a) <= ANGLE_BOOST and d > DIST_BOOST and self.boost == 1:
        #         thurst = "BOOST"
        #         self.boost = 0
        #     else :
        #         thurst = THRUST_MAX

        # debug("dist:",d)
        # debug("angle:",a)
        # debug("boost:", self.boost)
        # debug("thurst:",thurst)

        # #on save les coordonnées du pod dans px py pour le tour d'après
        # self.px,self.py = pod_x, pod_y

        # print(X,Y,thurst)



# INSTANCIATION
game = Game()

# GAME LOOP
while True:
    game.run()
