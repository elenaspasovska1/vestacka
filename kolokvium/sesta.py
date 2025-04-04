from searching_framework.uninformed_search import Problem
from searching_framework.uninformed_search import *
"""На табла со димензии N x N, каде N > 3 е непарен природен број, поставени се топчиња

    На влез прво се чита должина и ширина на просторот. Потоа се чита бројот на топчиња.
    Во наредните линии се читаат позициите на топчињата.
    На крај се читаат бројот на препреките и во наредна линија позиција на препрека."""

"""state=(balls tuples)"""
def check_valid(state,n, obstacles):
    unique_positions = set(state)
    if len(unique_positions) != len(state):
        return False
    for x,y in state:
        if not(0<=x<n and 0<=y<n and (x,y) not in obstacles and (x,y)):
            return False
    return True
"""gore desno"""
def goreDesno(index, state):
    balls=list(state)
    x,y=balls[index]
    if (x+1,y+1) in balls:
        balls.remove((x+1,y+1))
        balls.append((x+2,y+2))
        balls.remove(balls[index])
    return tuple(balls)
"""gore levo"""
def goreLevo(index, state):
    balls=list(state)
    x,y=balls[index]
    if (x-1,y+1) in balls:
        balls.remove((x-1,y+1))
        balls.append((x-2,y+2))
        balls.remove(balls[index])
    return tuple(balls)
"""dolu levo"""
def doluLevo(index, state):
    balls=list(state)
    x,y=balls[index]
    if (x-1,y-1) in balls:
        balls.remove((x-1,y-1))
        balls.append((x-2,y-2))
        balls.remove(balls[index])
    return tuple(balls)
"""dolu desno"""
def doluDesno(index, state):
    balls=list(state)
    x,y=balls[index]
    if (x+1,y-1) in balls:
        balls.remove((x+1,y-1))
        balls.append((x+2,y-2))
        balls.remove(balls[index])
    return tuple(balls)
"""levo"""
def levo(index, state):
    balls=list(state)
    x,y=balls[index]
    if (x-1,y) in balls:
        balls.remove((x-1,y))
        balls.append((x-2,y))
        balls.remove(balls[index])
    return tuple(balls)
"""desno"""
def desno(index, state):
    balls=list(state)
    x,y=balls[index]
    if (x+1,y) in balls:
        balls.remove((x+1,y))
        balls.append((x+2,y))
        balls.remove(balls[index])
    return tuple(balls)

class Topcinja(Problem):
    def __init__(self, initial, obstacles,grid):
        super().__init__(initial)
        self.obstacles = obstacles
        self.n=grid
    def successor(self, state):
        successors = dict()
        state_list = list(state)

        """((x,y),(x,y),(x,y),(x,y),(x,y),(x,y),..)"""
        for i in range(len(state)):
            x, y = state_list[i]
            """gore desno"""
            tmp_list=state_list[:]
            new_state=goreDesno(i,tmp_list)
            if check_valid(new_state,self.n, self.obstacles):
                if list(new_state) != tmp_list:
                    successors["GoreDesno: (x:"+str(x)+", y:"+str(y)+")" ] = new_state
            """gore levo"""
            tmp_list = list(state_list)
            new_state = goreLevo(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if list(new_state) != tmp_list:
                    successors["GoreLevo: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """dolu levo"""
            tmp_list = state_list[:]
            new_state = doluLevo(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if list(new_state) != tmp_list:
                    successors["DoluLevo: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """dolu desno"""
            tmp_list = state_list[:]
            new_state = doluDesno(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if list(new_state) != tmp_list:
                    successors["DoluDesno: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """desno"""
            tmp_list = state_list[:]
            new_state = desno(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if list(new_state) != tmp_list:
                    successors["Desno: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            """levo"""
            tmp_list = state_list[:]
            new_state = levo(i, tmp_list)
            if check_valid(new_state, self.n, self.obstacles):
                if list(new_state) != tmp_list:
                    successors["Levo: (x:" + str(x) + ", y:" + str(y) + ")"] = new_state
            #print(state)
            #print(successors)
        return successors

    def actions(self, state):
        #print(self.successor(state).keys())
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        balls=state
        return len(balls)==1 and (int(self.n/2), self.n-1) in balls

if __name__ == '__main__':
    n=int(input())
    b=int(input())
    ini=[]
    for s in range(b):
        ini.append(tuple(map(int,input().split(','))))
    k=int(input())
    ob=[]
    for q in range(k):
        ob.append(tuple(map(int,input().split(','))))

    problem = Topcinja(tuple(ini),tuple(ob),n)
    result=breadth_first_graph_search(problem)
    print(result.solution())
