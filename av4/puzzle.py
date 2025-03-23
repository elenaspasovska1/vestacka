from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search

class Puzzle(Problem):
    def __init__(self, initial, goal=None):
        super().__init__(initial, goal)

    def successor(self, state):
        succ={}
        """state = *32415678
                    0 1 2
                    3 4 5 
                    6 7 8 
           action=moving the *
        """
        ind=state.index("*")
        #Up - swap(i-3, i)
        if ind >= 3:
            tmp=list(state)
            tmp[ind], tmp[ind-3] = tmp[ind-3], tmp[ind]
            new_state="".join(tmp)
            succ["Up"]=new_state
        #Down - swap(i,i+3)
        if ind<=5:
            tmp = list(state)
            tmp[ind], tmp[ind + 3] = tmp[ind + 3], tmp[ind]
            new_state = "".join(tmp)
            succ["Down"] = new_state
        #Left - swap(i,i-1)
        if ind % 3 != 0:
            tmp = list(state)
            tmp[ind], tmp[ind-1] = tmp[ind-1], tmp[ind]
            new_state = "".join(tmp)
            succ["Left"] = new_state
        #Right - swap(i,i+1)
        if ind % 3 != 2:
            tmp = list(state)
            tmp[ind], tmp[ind + 1] = tmp[ind + 1], tmp[ind]
            new_state = "".join(tmp)
            succ["Right"] = new_state
        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        counter = 0 #kolku se na vistinskoto mesto hamingovo rastojanie
        for x,y in zip(node.state, self.goal):
            if x != y:
                counter += 1
        return counter

class PuzzleH2(Puzzle):
    coordinates={ 0: (1,2), 1: (1,2), 2: (2,2),
                  3: (0,1), 4: (1,1), 5: (2,1),
                  6: (0,0), 7: (1,0), 8: (2,0)}

    @staticmethod
    def mhd(n, m):#jasno
        x1, y1 = PuzzleH2.coordinates[n]
        x2, y2 = PuzzleH2.coordinates[m]
        return abs(x1-x2) + abs(y1-y2)

    def h(self, node):#kolku vkupno cekori se potrebni za da se namestat site na vistinskoto mesto
        sum_value = 0
        for x in "12345678":
            val = PuzzleH2.mhd(node.state.index(x), int(x))
            sum_value += val
        return sum_value


if __name__ == '__main__':
    puzzle = PuzzleH2("*32415678", "*12345678")
    result1 = greedy_best_first_graph_search(puzzle)
    print(result1.solve())
    result2 = astar_search(puzzle)
    print(result2.solve())
    result3 = recursive_best_first_search(puzzle)
    print(result3.solve())
