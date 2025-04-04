from searching_framework import best_first_graph_search
from searching_framework.uninformed_search import *
from searching_framework.utils import *

"""само еден блок од врвот на некој столб може да
   се помести на некој друг столб ако е помал од блокот
   на врвот на другиот столб или другиот столб е празен"""

def valid_move(pillar1,pillar2):
    """from pillar1 to pillar2"""
    if len(pillar1) != 0:
        last_in_p1=pillar1[-1]
    else:
        return False
    if len(pillar2) != 0:
        last_in_p2=pillar2[-1]
    else:
        last_in_p2=float('inf') #is empty
    return last_in_p1 <= last_in_p2

def move(pillar1,pillar2):
    new_p1, new_p2 = list(pillar1), list(pillar2)
    to_move=new_p1.pop()
    new_p2.append(to_move)
    return new_p1,new_p2

class Pillars(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)
        self.goal = goal
    def successor(self, state):
        #successors=dict()
        #p1,p2,p3 = list(state[0]), list(state[1]), list(state[2])
        #"""p1->p2"""
        #if valid_move(p1,p2):
        #    new_p1,new_p2=move(p1,p2)
        #    successors["MOVE TOP BLOCK FROM PILLAR 1 TO PILLAR 2"]=(tuple(new_p1), tuple(new_p2),tuple(p3))
        #"""p1->p3"""
        #if valid_move(p1,p3):
        #    new_p1,new_p3=move(p1,p3)
        #    successors["MOVE TOP BLOCK FROM PILLAR 1 TO PILLAR 3"]=(tuple(new_p1), tuple(p2),tuple(new_p3))
        #"""p2->p3"""
        #if valid_move(p2,p3):
        #    new_p2,new_p3=move(p2,p3)
        #    successors["MOVE TOP BLOCK FROM PILLAR 2 TO PILLAR 3"]=(tuple(p1), tuple(new_p2),tuple(new_p3))
        #"""p2->p1"""
        #if valid_move(p2,p1):
        #    new_p2,new_p1=move(p2,p1)
        #    successors["MOVE TOP BLOCK FROM PILLAR 2 TO PILLAR 1"]=(tuple(new_p1), tuple(new_p2),tuple(p3))
        #"""p3->p1"""
        #if valid_move(p3, p1):
        #    new_p3, new_p1 = move(p3, p1)
        #    successors["MOVE TOP BLOCK FROM PILLAR 3 TO PILLAR 1"] = (tuple(new_p1), tuple(p2), tuple(new_p3))
        #"""p3->p2"""
        #if valid_move(p3, p2):
        #    new_p3, new_p2 = move(p3, p2)
        #    successors["MOVE TOP BLOCK FROM PILLAR 3 TO PILLAR 2"] = (tuple(p1), tuple(new_p2), tuple(new_p3))
        successors = dict()
        n = len(state)  # Number of pillars

        # Try moving from each pillar to every other pillar
        for i in range(n):
            for j in range(n):
                if i != j and valid_move(state[i], state[j]):
                    new_state = list(state)
                    new_p1, new_p2 = move(state[i], state[j])
                    new_state[i], new_state[j] = tuple(new_p1), tuple(new_p2)
                    action = f"Move top block from Pillar {i + 1} to Pillar {j + 1}"
                    successors[action] = tuple(new_state)

        return successors
    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return tuple(state) == tuple(self.goal)

if __name__ == '__main__':
    #s=((3,2,1),(),())
    #g=((),(),(3,2,1))
    ini=[]
    ss=input().split(';')
    for s in ss:
        if len(s)==0:
            ini.append(tuple())
        else:
            ini.append(tuple(map(int,s.split(','))))
    goal=[]
    gs=input().split(';')
    for g in gs:
        if len(g)==0:
            goal.append(tuple())
        else:
            goal.append(tuple(map(int,g.split(','))))

    #print(ini)
    #print(goal)
    problem = Pillars(tuple(ini), tuple(goal))
    sol = breadth_first_graph_search(problem)
    if sol:
        print("Number of action " + str(len(sol.solution())))
    print(sol.solution())