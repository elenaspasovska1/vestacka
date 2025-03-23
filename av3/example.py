from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):
        """recnik mozni akcija-sostojba"""
        """(j0, j1)"""
        successors = dict()

        j0,j1=state
        c0,c1=self.capacities

        #praznenje
        if j0>0:
            successors["Isprazni go j0"]=(0,j1)
        if j1>0:
            successors["Isprazni go j1"]=(j0,0)

        #preturanje
        if j0>0 and j1<c1:
            delta=min(c1-j1, j0)
            successors["Preturi od j0 vo j1"]=(j0-delta, j1+delta)

        if j1>0 and j0<c0:
            delta=min(c0-j0, j1)
            successors["Preturi od j1 vo j0"]=(j0+delta, j1-delta)

        #polnenje
        if j0 < c0:
            successors["Napolni j0"] = (c0, j1)
        if j1 < c1:
            successors["Napolni j1"] = (j0, c1)

        return successors

    def actions(self, state):
        """lista mozni akcii od momentalen state"""
        """za successor ni treba samo key"""
        return self.successor(state).keys()


    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return self.goal==state

if __name__ == "__main__":
    container = Container([15,5], (5,5), (10,0))

    result= breadth_first_graph_search(container)

    print(result.solution())
    print(result.solve())
