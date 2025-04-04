from searching_framework.utils import Problem
from searching_framework.informed_search import *

def check_valid(state):
    man_x, man_y, house_x, house_y, obsticles, grid = state
    if 0 <= man_x < grid and 0 <= man_y < grid:
        if (man_x, man_y) not in obsticles:
            return True
    return False

#state=(man_x,man_y, house_x, house_y, obsticles, grid)
class Maze(Problem):
    def __init__(self, initial):
        super().__init__(initial)
    def successor(self, state):
        successors=dict()
        man_x, man_y, house_x, house_y, obsticles, grid = state
        """desno 2"""
        state_on_move=(man_x+1, man_y, house_x, house_y, obsticles, grid)
        new_state=(man_x+2, man_y, house_x, house_y, obsticles, grid)
        if check_valid(state_on_move) and check_valid(new_state):
            successors["Desno 2"] = new_state
        """desno 3"""
        state_on_move = (man_x + 1, man_y, house_x, house_y, obsticles, grid)
        state_on_move_2 = (man_x + 2, man_y, house_x, house_y, obsticles, grid)
        new_state = (man_x + 3, man_y, house_x, house_y, obsticles, grid)
        if check_valid(state_on_move) and check_valid(state_on_move_2) and check_valid(new_state):
            successors["Desno 3"] = new_state
        """gore"""
        new_state = (man_x, man_y+1, house_x, house_y, obsticles, grid)
        if check_valid(new_state):
            successors["Gore"] = new_state
        """Dolu"""
        new_state = (man_x, man_y-1, house_x, house_y, obsticles, grid)
        if check_valid(new_state):
            successors["Dolu"] = new_state
        """levo"""
        new_state = (man_x-1, man_y, house_x, house_y, obsticles, grid)
        if check_valid(new_state):
            successors["Levo"] = new_state
        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return (state[0],state[1])==(state[2],state[3])
    def h(self,node):
        return abs(node.state[0]-node.state[2])/3 +abs(node.state[1]-node.state[3])

if __name__ == "__main__":
    mgrid=int(input())
    n=input()
    mobsticles=[]
    for i in range(int(n)):
        o_x, o_y = map(int, input().split(","))
        mobsticles.append((o_x, o_y))
    mman_x, mman_y = map(int, input().split(","))
    mhouse_x, mhouse_y = map(int, input().split(","))

    lavirint=Maze((mman_x, mman_y, mhouse_x, mhouse_y, tuple(mobsticles),mgrid))
    result= astar_search(lavirint)
    if(result):
        print(result.solution())
    else:
        print("No solution!")
