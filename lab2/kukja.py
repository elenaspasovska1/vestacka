from searching_framework.utils import Problem
from searching_framework.informed_search import *
import math
def check_valid(state):
    man_x,man_y,house_x,house_y,house_dir,allowed = state
    if 0 <= man_x < 5 and 0 <= man_y < 9 and 0 <= house_x < 5:
        if (man_x, man_y) in allowed or (man_x, man_y) == (house_x, house_y):
            return True
    return False
def move_house(state):
    man_x,man_y,house_x,house_y,house_dir,allowed = state
    if house_x == 4 and house_dir == "desno":
        house_dir = "levo"
    if house_x == 0 and house_dir == "levo":
        house_dir = "desno"

    if house_dir == 'desno':
        return house_x+1, house_dir
    else:
        return house_x-1, house_dir


#state=(man_x,man_y,house_x,house_y,house_dir,allowed)
class House(Problem):
    def __init__(self, initial):
        super().__init__(initial)

    def successor(self, state):
        man_x, man_y, house_x, house_y, house_dir, allowed = state
        successors=dict()

        new_house_x = move_house(state)[0]
        new_house_dir = move_house(state)[1]
        """stoj"""
        new_state=(man_x, man_y, new_house_x, house_y, new_house_dir, allowed)
        if check_valid(new_state):
            successors["Stoj"]=new_state
        """gore 1 """

        new_state=(man_x, man_y+1, new_house_x, house_y, new_house_dir, allowed)
        if check_valid(new_state):
            successors["Gore 1"]=new_state
        """gore 2 """
        new_state = (man_x, man_y + 2, new_house_x, house_y, new_house_dir, allowed)
        if check_valid(new_state):
            successors["Gore 2"] = new_state
        """gore-desno 1"""
        new_state = (man_x + 1, man_y + 1, new_house_x, house_y, new_house_dir, allowed)
        if check_valid(new_state):
            successors["Gore desno 1"] = new_state
        """gore desno 2"""
        new_state = (man_x + 2, man_y + 2, new_house_x, house_y, new_house_dir, allowed)
        if check_valid(new_state):
            successors["Gore desno 2"] = new_state
        """gore-levo 1"""
        new_state = (man_x - 1, man_y + 1, new_house_x, house_y, new_house_dir, allowed)
        if check_valid(new_state):
            successors["Gore levo 1"] = new_state
        """gore levo 2"""
        new_state = (man_x - 2, man_y + 2, new_house_x, house_y, new_house_dir, allowed)
        if check_valid(new_state):
            successors["Gore levo 2"] = new_state
        return successors


    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        man_x, man_y, house_x, house_y, house_dir, allowed = state
        return (man_x, man_y) == (house_x, house_y)

    def h(self, node):
        x_man = node.state[0]
        y_man = node.state[1]
        x_h=node.state[2]
        y_h=node.state[3]
        return (y_h- y_man)/2

if __name__ == '__main__':
    m_allowed=[(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
                   (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    mman_x, mman_y = map(int, input().split(","))
    mhouse_x, mhouse_y = map(int, input().split(","))
    mhouse_dir = input()
    kukja = House((mman_x,mman_y,mhouse_x,mhouse_y,mhouse_dir,tuple(m_allowed)))
    result = greedy_best_first_graph_search(kukja)
    if(result):
        print(result.solution())
    else:
        print("No Solution!")