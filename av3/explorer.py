from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Explorer(Problem):
    """initial= ((xc,yc),(x1,y1,n1),(x2,y2,n2))"""
    def __init__(self, initial,goal=None):
        super().__init__(initial, goal)
        self.grid_size=[8,6]

    def successor(self, state):
        #n=-1down
        #n-1 up

        #((xc,yc),(x1,y1,n1),(x2,y2,n2))
        x_c=state[0]
        y_c=state[1]
        obstacle1= list(state[2])
        obstacle2= list(state[3])

        #dvizenje na preckite
        #obstacle1
        if obstacle1[2]==1: #up
            if obstacle1[1] == self.grid_size[1]-1: #dali e maksimalnata sto moze da ja ima
                obstacle1[2] = -1
                obstacle1[1] -= 1
            else: obstacle1[1] += 1
        else: #down
            if obstacle1[1] == 0:
                obstacle1[2] = 1
                obstacle1[1] += 1
            else:
                obstacle1[1] -=1
        #obstacle2
        if obstacle2[2] == 1: #up
            if obstacle2[1] == self.grid_size[1]-1:
                obstacle2[2] = -1
                obstacle2[1] -= 1
            else: obstacle2[1] += 1
        else: #down
            if obstacle2[1] == 0:
                obstacle2[2] = 1
                obstacle2[1] += 1
            else:
                obstacle2[1] -= 1

        obstacles=[(obstacle1[0],obstacle1[1]),(obstacle2[0],obstacle2[1])]

        #dvizenje na coveceto
        sucessors=dict()
        #right x=x+1
        if x_c+1 < self.grid_size[0] and (x_c+1, y_c) not in obstacles:
            sucessors["Right"] = (x_c+1, y_c, (obstacle1[0],obstacle1[1], obstacle1[2]), (obstacle2[0],obstacle2[1], obstacle2[2]))

        if x_c > 0 and (x_c-1, y_c) not in obstacles:
            sucessors["Left"] = (x_c-1, y_c, (obstacle1[0],obstacle1[1], obstacle1[2]), (obstacle2[0],obstacle2[1], obstacle2[2]))

        if y_c+1 < self.grid_size[1] and (y_c+1, y_c) not in obstacles:
            sucessors["Up"] = (x_c, y_c+1, (obstacle1[0],obstacle1[1], obstacle1[2]), (obstacle2[0],obstacle2[1], obstacle2[2]))

        if y_c > 0 and (y_c-1, y_c) not in obstacles:
            sucessors["Down"] = (x_c, y_c-1, (obstacle1[0],obstacle1[1], obstacle1[2]), (obstacle2[0],obstacle2[1], obstacle2[2]))

        return sucessors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0]==self.goal[0] and state[1]==self.goal[1]

if __name__ == '__main__':
    goal_state = (7,4)
    initial_state = (0,2)
    obstacle_1=(2, 5, -1)
    obstacle_2=(5, 0, 1)

    explorer = Explorer((initial_state[0],initial_state[1], obstacle_1, obstacle_2), goal_state)
    result= breadth_first_graph_search(explorer)
    print(result.solution())
    print(result.solve())