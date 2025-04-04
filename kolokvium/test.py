from searching_framework.uninformed_search import Problem
from searching_framework.uninformed_search import *
def check_valid(state, n, obstacles):
    unique_positions = set(state)
    if len(unique_positions) != len(state):
        return False
    for x, y in state:
        if not (0 <= x < n and 0 <= y < n) or (x, y) in obstacles:
            return False
    return True

"""gore desno"""
def goreDesno(index, state):
    balls = list(state)
    x, y = balls[index]
    if (x + 1, y + 1) in balls:
        if (x+2,y+2) not in balls:
            balls.remove((x + 1, y + 1))
            balls[index] = (x+2,x+2)
    return tuple(balls)

"""gore levo"""
def goreLevo(index, state):
    balls = list(state)
    x, y = balls[index]
    if (x - 1, y + 1) in balls:
        balls.remove((x - 1, y + 1))
        balls[index] = (x - 2, y + 2)
    return tuple(balls)

"""dolu levo"""
def doluLevo(index, state):
    balls = list(state)
    x, y = balls[index]
    if (x - 1, y - 1) in balls:
        balls.remove((x - 1, y - 1))
        balls[index] = (x - 2, y - 2)
    return tuple(balls)

"""dolu desno"""
def doluDesno(index, state):
    balls = list(state)
    x, y = balls[index]
    if (x + 1, y - 1) in balls:
        balls.remove((x + 1, y - 1))
        balls[index] = (x + 2, y - 2)
    return tuple(balls)

"""levo"""
def levo(index, state):
    balls = list(state)
    x, y = balls[index]
    if (x - 1, y) in balls:
        balls.remove((x - 1, y))
        balls[index] = (x - 2, y)
    return tuple(balls)

"""desno"""
def desno(index, state):
    balls = list(state)
    x, y = balls[index]
    if (x + 1, y) in balls:
        balls.remove((x + 1, y))
        balls[index] = (x + 2, y)
    return tuple(balls)

class Topcinja(Problem):
    def __init__(self, initial, obstacles, grid):
        super().__init__(initial)
        self.obstacles = obstacles
        self.n = grid

    def successor(self, state):
        successors = dict()
        state_list = list(state)

        """((x,y),(x,y),(x,y),(x,y),(x,y),(x,y),..)"""
        for i in range(len(state)):
            x, y = state_list[i]
            """gore desno"""
            tmp_list = list(state_list)
            new_state = goreDesno(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if new_state != tuple(tmp_list):
                    successors["GoreDesno: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """gore levo"""
            tmp_list = list(state_list)
            new_state = goreLevo(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if new_state != tuple(tmp_list):
                    successors["GoreLevo: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """dolu levo"""
            tmp_list = list(state_list)
            new_state = doluLevo(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if new_state != tuple(tmp_list):
                    successors["DoluLevo: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """dolu desno"""
            tmp_list = list(state_list)
            new_state = doluDesno(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if new_state != tuple(tmp_list):
                    successors["DoluDesno: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """desno"""
            tmp_list = list(state_list)
            new_state = desno(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if new_state != tuple(tmp_list):
                    successors["Desno: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """levo"""
            tmp_list = list(state_list)
            new_state = levo(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if new_state != tuple(tmp_list):
                    successors["Levo: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        balls = state
        return len(balls) == 1 and (int(self.n / 2), self.n - 1) in balls

if __name__ == '__main__':
    n = int(input())
    b = int(input())
    ini = []
    for s in range(b):
        ini.append(tuple(map(int, input().split(','))))
    k = int(input())
    ob = []
    for q in range(k):
        ob.append(tuple(map(int, input().split(','))))

    problem = Topcinja(tuple(ini), tuple(ob), n)
    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No solution found.")
