from searching_framework import breadth_first_graph_search
from searching_framework.utils import Problem
from searching_framework.uninformed_search import *
class Squares(Problem):
    def __init__(self, initial, house):
        super().__init__(initial, house)

    def goal_test(self, state):
        return state == self.goal

    @staticmethod
    def check_valid(state):
        for x, y in state:
            if x < 0 or x > 4 or y < 0 or y > 4:
                return False
        return True
    @staticmethod
    def my_check_valid(state):
        x, y = state
        if x < 0 or x > 4 or y < 0 or y > 4:
            return False
        return True

    def successor(self, state):
        succ = dict()
        stateList = list(state)
        for i in range(5):
            """move up"""
            new_s = (stateList[i][0],stateList[i][1]+1)
            if Squares.my_check_valid(new_s):
                temp_state = stateList[:]
                temp_state[i] = new_s
                succ["Pomesti kvadratche "+str(i+1)+" gore"] = tuple(temp_state)
            """move down"""
            new_s = (stateList[i][0],stateList[i][1]-1)
            if Squares.my_check_valid(new_s):
                temp_state = stateList[:]
                temp_state[i] = new_s
                succ["Pomesti kvadratche "+str(i+1)+" dolu"] = tuple(temp_state)
            """move left"""
            new_s = (stateList[i][0]-1,stateList[i][1])
            if Squares.my_check_valid(new_s):
                temp_state = stateList[:]
                temp_state[i] = new_s
                succ["Pomesti kvadratche "+str(i+1)+" levo"] = tuple(temp_state)
            """move right"""
            new_s = (stateList[i][0]+1,stateList[i][1])
            if Squares.my_check_valid(new_s):
                temp_state = stateList[:]
                temp_state[i] = new_s
                succ["Pomesti kvadratche "+str(i+1)+" desno"] = tuple(temp_state)
        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]



if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))
    ini = []
    for _ in range(5):
        ini.append(tuple(map(int, input().split(','))))

    goal_state = ((0, 4), (1, 3), (2, 2), (3, 1), (4, 0))

    squares = Squares(tuple(ini), goal_state)
    result=breadth_first_graph_search(squares)
    print(result.solution())

    def h(self,node):
        moves_to_goal=0
        sq = node.state
        goal = self.goal
        for i in range(5):
            s=sq[i]
            g=goal[i]
            moves_to_goal += abs(g[0]-s[0])+abs(g[1]-s[1])
        return moves_to_goal


