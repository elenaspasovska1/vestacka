from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def k1(x, y, b_x, b_y):#gore gore levo
    if 0 <= x-1 < 8 and 0 < y+2 < 8 and [x-1,y+2]!=[b_x, b_y]:
        x-=1
        y+=2
    return x,y
def k2(x, y, b_x, b_y):#gore gore desno
    if 0 <= x+1 < 8 and 0 < y+2 < 8 and [x+1,y+2]!=[b_x, b_y]:
        x+=1
        y+=2
    return x,y
def k3(x, y, b_x, b_y):#desno desno gore
    if 0 <= x+2 < 8 and 0 < y+1 < 8 and [x+2,y+1]!=[b_x, b_y]:
        x+=2
        y+=1
    return x,y
def k4(x, y, b_x, b_y):#desno desno dole
    if 0 <= x+2 < 8 and 0 < y-1 < 8 and [x+2,y-1]!=[b_x, b_y]:
        x+=2
        y-=1
    return x,y
def k5(x, y, b_x, b_y):#dole dole desno
    if 0 <= x+1 < 8 and 0 < y-2 < 8 and [x+1,y-2]!=[b_x, b_y]:
        x+=1
        y-=2
    return x,y
def k6(x, y, b_x, b_y):#dole dole levo
    if 0 <= x-1 < 8 and 0 < y-2 < 8 and [x-1,y-2]!=[b_x, b_y]:
        x-=1
        y-=2
    return x,y
def k7(x, y, b_x, b_y):#levo levo dole
    if 0 <= x-2 < 8 and 0 < y-1 < 8 and [x-2,y-1]!=[b_x, b_y]:
        x-=2
        y-=1
    return x,y
def k8(x, y, b_x, b_y):#levo levo gore
    if 0 <= x-2 < 8 and 0 < y+1 < 8 and [x-2,y+1]!=[b_x, b_y]:
        x-=2
        y+=1
    return x,y

def b1(x,y,k_x,k_y):#gore levo
    if 0<=x-1<8 and 0<y+1<8 and [x-1, y+1] != [k_x, k_y]:
        x-=1
        y+=1
    return x,y
def b2(x,y,k_x,k_y):#gore desno
    if 0<=x+1<8 and 0<y+1<8 and [x+1, y+1] != [k_x, k_y]:
        x+=1
        y+=1
    return x,y
def b3(x,y,k_x,k_y):#dolu levo
    if 0<=x-1<8 and 0<y-1<8 and [x-1, y-1] != [k_x, k_y]:
        x-=1
        y-=1
    return x,y
def b4(x,y,k_x,k_y):#dole desno
    if 0<=x+1<8 and 0<y-1<8 and [x+1, y-1] != [k_x, k_y]:
        x+=1
        y-=1
    return x,y

class Stars(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        #(kx,ky,bx,by,((star1x, star1y),...))
        knight_x, knight_y=state[0], state[1]
        bishop_x, bishop_y=state[2], state[3]
        star_pos=state[4]
        sucessors= dict()

        x_new, y_new = k1(knight_x, knight_y, bishop_x, bishop_y)
        if [x_new, y_new] != [knight_x, knight_y]:
            sucessors["k1"]=(x_new, y_new, bishop_x, bishop_y, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = k2(knight_x, knight_y, bishop_x, bishop_y)
        if [x_new, y_new] != [knight_x, knight_y]:
            sucessors["k2"] = (
            x_new, y_new, bishop_x, bishop_y, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = k3(knight_x, knight_y, bishop_x, bishop_y)
        if [x_new, y_new] != [knight_x, knight_y]:
            sucessors["k3"] = (
            x_new, y_new, bishop_x, bishop_y, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = k4(knight_x, knight_y, bishop_x, bishop_y)
        if [x_new, y_new] != [knight_x, knight_y]:
            sucessors["k4"] = (
            x_new, y_new, bishop_x, bishop_y, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = k5(knight_x, knight_y, bishop_x, bishop_y)
        if [x_new, y_new] != [knight_x, knight_y]:
            sucessors["k5"] = (
            x_new, y_new, bishop_x, bishop_y, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = k6(knight_x, knight_y, bishop_x, bishop_y)
        if [x_new, y_new] != [knight_x, knight_y]:
            sucessors["k6"] = (
            x_new, y_new, bishop_x, bishop_y, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = k7(knight_x, knight_y, bishop_x, bishop_y)
        if [x_new, y_new] != [knight_x, knight_y]:
            sucessors["k7"] = (
            x_new, y_new, bishop_x, bishop_y, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = k8(knight_x, knight_y, bishop_x, bishop_y)
        if [x_new, y_new] != [knight_x, knight_y]:
            sucessors["k8"] = (
            x_new, y_new, bishop_x, bishop_y, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = b1(bishop_x, bishop_y, knight_x, knight_y)
        if [x_new, y_new] != [bishop_x, bishop_y]:
            sucessors["b1"] = (
            knight_x, knight_y, x_new, y_new, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = b2(bishop_x, bishop_y, knight_x, knight_y)
        if [x_new, y_new] != [bishop_x, bishop_y]:
            sucessors["b2"] = (
                knight_x, knight_y, x_new, y_new, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = b3(bishop_x, bishop_y, knight_x, knight_y)
        if [x_new, y_new] != [bishop_x, bishop_y]:
            sucessors["b3"] = (
                knight_x, knight_y, x_new, y_new, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))

        x_new, y_new = b4(bishop_x, bishop_y, knight_x, knight_y)
        if [x_new, y_new] != [bishop_x, bishop_y]:
            sucessors["b4"] = (
                knight_x, knight_y, x_new, y_new, tuple([s for s in star_pos if (s[0], s[1]) != (x_new, y_new)]))
        return sucessors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return len(state[4]) == 0

if __name__ == "__main__":
    knight=[2,5]
    bishop=[5,1]
    stars_pos=((1,1),(4,3),(6,6))
    stars=Stars((knight[0],knight[1], bishop[0], bishop[1], stars_pos))
    result=breadth_first_graph_search(stars)
    print(result.solve())
    print(result.solution())