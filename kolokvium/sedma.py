from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class CrnobeloProblem(Problem):
    def __init__(self, initial,grid):
        Problem.__init__(self, initial)
        self.grid = grid
    @staticmethod
    def make_matrix(blaks, grid):
        marix={}
        for i in range(grid):
            for j in range(grid):
                pass


    def successor(self, state):
        successors=dict()
        black=list(state)




    def actions(self, state):
        # print(self.successor(state).keys())
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        balls = state
        return len(balls) == 1 and (int(self.n / 2), self.n - 1) in balls

