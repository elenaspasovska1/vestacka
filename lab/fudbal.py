from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def check_valid(fstate, opponents):
    """state=(man_x, man_y, ball_x, ball_y)
    coveceto ne moze da se nagja vo isto pole so topkata ili protivnicite
    topkata ne moze da se naogja vo pole koe e sosedno so nekoi od protivnicite
    """
    fman_x, fman_y, fball_x, fball_y=fstate
    if not(0 <= fman_x < 8 and 0 <= fman_y < 6 and 0 <= fball_x < 8 and 0 <= fball_y < 6):
        return False
    if (fman_x, fman_y) == (fball_x, fball_y) or (fman_x, fman_y) in opponents:
        return False
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if (fball_x+x, fball_y+y) in opponents:
                return False
    # if (state[2], state[3]) in opponents or (state[2]-1, state[3]+1) in opponents or (state[2], state[3]+1) in opponents or (state[2]+1, state[3]+1) in opponents or (state[2]-1, state[3]) in opponents or (state[2]+1, state[3]) or (state[2]-1, state[3]-1) in opponents or (state[2], state[3]-1) or (state[2]+1,state[3]-1) in opponents:
    #     return False
    return True


class Football(Problem):
    #state=(man_x, man_y, ball_x, ball_y)
    def __init__(self, initial):
        super().__init__(initial, ((7,2), (7,3)))
        self.opponents = ((3,3), (5,4))
        self.grid = (8,6)

    def successor(self, state):
        man_x, man_y, ball_x, ball_y = state
        successors=dict()
        if abs(man_x - ball_x) <=1 and abs(man_y - ball_y) <=1: #vo okolina na topkata e
            """turni gore"""
            if man_y+1 == ball_y and man_x==ball_x:
                state_new = (man_x, man_y+1, ball_x, ball_y+1)
                if check_valid(state_new, self.opponents):
                    successors["Turni topka gore"] = state_new
            """turni dole"""
            if man_y == ball_y+1 and man_x==ball_x:
                state_new = (man_x, man_y-1, ball_x, ball_y-1)
                if check_valid(state_new, self.opponents):
                    successors["Turni topka dolu"] = state_new
            """turni desno"""
            if man_y == ball_y and man_x+1 == ball_x:
                state_new = (man_x+1, man_y, ball_x+1, ball_y)
                if check_valid(state_new, self.opponents):
                    successors["Turni topka desno"] = state_new
            """turni gore-desno"""
            if man_x+1 == ball_x and man_y+1 == ball_y:
                state_new = (man_x+1, man_y+1, ball_x+1, ball_y+1)
                if check_valid(state_new, self.opponents):
                    successors["Turni topka gore-desno"] = state_new
            """turni dolu-desno"""
            if man_x+1 == ball_x and man_y-1 == ball_y:
                state_new = (man_x+1, man_y-1, ball_x+1, ball_y-1)
                if check_valid(state_new, self.opponents):
                    successors["Turni topka dolu-desno"] = state_new

        #else: #dvizi se sam bez topkata
        """odi gore"""
        state_new = (man_x, man_y+1, ball_x, ball_y)
        if check_valid(state_new, self.opponents):
            successors["Pomesti coveche gore"] = state_new
        """odi dole"""
        state_new = (man_x, man_y-1, ball_x, ball_y)
        if check_valid(state_new, self.opponents):
            successors["Pomesti coveche dolu"] = state_new
        """odi desno"""
        state_new = (man_x+1, man_y, ball_x, ball_y)
        if check_valid(state_new, self.opponents):
            successors["Pomesti coveche desno"] = state_new
        """odi gore-desno"""
        state_new = (man_x+1, man_y+1, ball_x, ball_y)
        if check_valid(state_new, self.opponents):
            successors["Pomesti coveche gore-desno"] = state_new
        """odi dolu-desno"""
        state_new = (man_x+1, man_y-1, ball_x, ball_y)
        if check_valid(state_new, self.opponents):
            successors["Pomesti coveche dolu-desno"] = state_new


        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return (state[2], state[3]) in self.goal

if __name__ == "__main__":
    """state=(man_x, man_y, ball_x, ball_y)"""
    mman_x, mman_y = map(int, input().split(","))
    mball_x, mball_y = map(int, input().split(","))

    mstate=(mman_x, mman_y, mball_x, mball_y)

    football=Football(mstate)
    result = breadth_first_graph_search(football)
    if(result):
        print(result.solution())
    else:
        print("No solution!")