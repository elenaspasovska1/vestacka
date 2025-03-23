from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search
def move_right(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 < 8 and [x1+1, y1] not in obstacles and [x1+1, y1] != [x2, y2] and [x1+1, y1] != [x3, y3]:
        x1 += 1
    return x1

def move_left(x1, y1, x2, y2, x3, y3, obstacles):
    while x1 > 0 and [x1-1, y1] not in obstacles and [x1-1, y1] != [x2, y2] and [x1-1, y1] != [x3, y3]:
        x1 += 1
    return x1

def move_up(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 < 6 and [x1, y1+1] not in obstacles and [x1, y1+1] != [x2, y2] and [x1, y1+1] != [x3, y3]:
        y1 += 1
    return y1

def move_down(x1, y1, x2, y2, x3, y3, obstacles):
    while y1 > 0 and [x1, y1-1] not in obstacles and [x1, y1-1] != [x2, y2] and [x1, y1-1] != [x3, y3]:
        y1 -= 1
    return y1


#state= (xh1,yh1,xo,yo,xh2,yh2)
class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = dict()

        x_h1, y_h1, x_o, y_o, x_h2, y_h2 = state

        #h1
        x_new=move_right(x_h1, y_h1, x_o, y_o, x_h2,y_h2, self.obstacles)
        if x_new != x_h1:
            successors["RightH1"]=(x_new, y_h1, x_o, y_o, x_h2, y_h2)
        x_new = move_left(x_h1, y_h1, x_o, y_o, x_h2, y_h2, self.obstacles)
        if x_new != x_h1:
            successors["LeftH1"] = (x_new, y_h1, x_o, y_o, x_h2, y_h2)
        y_new = move_up(x_h1, y_h1, x_o, y_o, x_h2, y_h2, self.obstacles)
        if y_new != y_h1:
            successors["UpH1"] = (x_h1, y_new, x_o, y_o, x_h2, y_h2)
        y_new = move_down(x_h1, y_h1, x_o, y_o, x_h2, y_h2, self.obstacles)
        if y_new != y_h1:
            successors["DownH1"] = (x_h1, y_new, x_o, y_o, x_h2, y_h2)

        #O
        x_new = move_right(x_o, y_o,x_h1, y_h1, x_h2, y_h2, self.obstacles)
        if x_new != x_h1:
            successors["RightH1"] = (x_new, y_h1, x_h2, y_h2, x_h1, y_h1)
        x_new = move_left( x_o, y_o,x_h1, y_h1, x_h2, y_h2, self.obstacles)
        if x_new != x_h1:
            successors["LeftH1"] = (x_new, y_h1, x_h2, y_h2, x_h1, y_h1)
        y_new = move_up( x_o, y_o,x_h1, y_h1, x_h2, y_h2, self.obstacles)
        if y_new != y_h1:
            successors["UpH1"] = (x_h1, y_new, x_h2, y_h2, x_h1, y_h1)
        y_new = move_down( x_o, y_o,x_h1, y_h1, x_h2, y_h2, self.obstacles)
        if y_new != y_h1:
            successors["DownH1"] = (x_h1, y_new, x_h2, y_h2, x_h1, y_h1)

        return successors



    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        h1 = state[0], state[1]
        o = state[2], state[3]
        h2 = state[4], state[5]

        value=0
        if h1[1] != o[1]:
            if h1[0] !=  (o[0]-1):
                value+=2
            else:
                value+=1
        else:
            if h1[0] > o[1]:
                value+=3
            elif h1[0] < (o[1]-1):
                value+=1

        if h2[1] != o[1]:
            if h2[0] !=  (o[0]+1):
                value+=2
            else:
                value+=1
        else:
            if h2[0] < o[1]:
                value+=3
            elif h2[0] > (o[1]-1):
                value+=1
        if h1[1] == h2[1] and h1[1] != o[1]:  # h1 i h2 vo ista redica, o vo razlicna
            value -= 1


    def goal_test(self, state):
        return
