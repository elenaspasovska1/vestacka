from lab2.kukja import check_valid
from searching_framework import breadth_first_graph_search
from searching_framework.utils import Problem
from searching_framework.informed_search import *

"""lavirint nxn
    dzidovi na slucajni pozicii, moze da se preskoknuvaat
    duhot se dvizi gore i desno za edna,dve ili tri pozicii
    
    input
    n 
    br_dzidovi
    pozicii_dzidovi
    pocetna duh e 0,0
    pocetna pakman n-1 n-1"""

class GhostOnSkates(Problem):
    def __init__(self, initial, walls, n, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.n = n

    def actions(self, state):
        return sorted(self.successor(state).keys())

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state, walls, n):
        x,y = state
        if 0<=x<n and 0<=y<n:
            if (x,y) not in walls:
                return True
        return False
    @staticmethod
    def gore(state, n):
        x,y = state
        return x,y+n
    @staticmethod
    def desno(state, n):
        x,y = state
        return x+n,y
    def successor(self, state):
        successors = dict()
        """nagore"""
        for i in range(1,4):
            new_state = GhostOnSkates.gore(state, i)
            if GhostOnSkates.check_valid(new_state,self.walls, self.n):
                successors["Gore "+str(i)] = new_state
        """desno"""
        for i in range(1,4):
            new_state = GhostOnSkates.desno(state, i)
            if GhostOnSkates.check_valid(new_state,self.walls, self.n):
                successors["Desno "+str(i)] = new_state
        return successors

    def h(self, node):
        x,y = node.state
        px,py = self.goal
        return abs(px-x)/3 + abs(py-y)/3


if __name__ == '__main__':
    n = int(input())
    ghost_pos = (0, 0)
    goal_pos = (n - 1, n - 1)

    num_holes = int(input())
    holes = list()
    for _ in range(num_holes):
        holes.append(tuple(map(int, input().split(','))))

    problem = GhostOnSkates(ghost_pos, holes, n, goal_pos)
    result = greedy_best_first_graph_search(problem)
    print(result.solution())

