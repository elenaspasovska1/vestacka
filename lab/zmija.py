from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def continueStraight(state):
    """state=(snake,green,red,orientation)
            =(((s1x,s1y), (s2x,s2y),..), ((g1x,g1y), (g2x,g2y),..), ((r1x,r1y), (r2x,r2y),..), ((str,str),(left,left), (right, right)))"""
    snake_fields, green_fields, red_fields, snake_orientation = list(state[0]), list(state[1]), list(state[2]), state[3]
    snake_head, snake_tail=snake_fields[-1], snake_fields[0]
    snake_orientation_mapped= Snake.orientation_map(snake_orientation)##(straight, right, left)
    delta = snake_orientation_mapped[0]
    new_head = (snake_head[0] + delta[0], snake_head[1] + delta[1])
    if 0 <= new_head[0]< 10 and 0 <= new_head[1] < 10:#ako ne iskaca
        if new_head not in red_fields:#ako ne se jade sama i ne jade crveno
            if new_head not in green_fields:#dali jade zeleno jabolko
                snake_fields.remove(snake_tail)#ako ne ne davaj da raste
            else:
                green_fields.remove(new_head)#ako jade trgni go zelenoto

            if new_head not in snake_fields:
                snake_fields.append(new_head)#dodadi od napred
                new_state=(tuple(snake_fields), tuple(green_fields), tuple(red_fields), snake_orientation)
                return new_state
    return state

def turnRight(state):
    snake_fields, green_fields, red_fields, snake_orientation = list(state[0]), list(state[1]), list(state[2]), state[3]
    snake_head, snake_tail = snake_fields[-1], snake_fields[0]
    snake_orientation_mapped = Snake.orientation_map(snake_orientation)  ##(straight, right, left)
    delta = snake_orientation_mapped[1]

    new_head = (snake_head[0] + delta[0], snake_head[1] + delta[1])
    if 0 <= new_head[0] < 10 and 0 <= new_head[1] < 10:  # ako ne iskaca
        if new_head not in red_fields:  # ako ne se jade sama
            if new_head not in green_fields:  # dali jade zeleno jabolko
                snake_fields.remove(snake_tail)
            else:
                green_fields.remove(new_head)

            if new_head not in snake_fields:
                snake_fields.append(new_head)#dodadi od napred
                new_orientation = "right" if snake_orientation == "up" else "down" if snake_orientation == "right" else "left" if snake_orientation == "down" else "up"
                new_state = (tuple(snake_fields), tuple(green_fields), tuple(red_fields), new_orientation)
                return new_state
    return state

def turnLeft(state):
    snake_fields, green_fields, red_fields, snake_orientation = list(state[0]), list(state[1]), list(state[2]), state[3]
    snake_head, snake_tail=snake_fields[-1], snake_fields[0]
    snake_orientation_mapped = Snake.orientation_map(snake_orientation)  ##(straight, right, left)
    delta = snake_orientation_mapped[2]

    new_head = (snake_head[0] + delta[0], snake_head[1] + delta[1])
    if 0 <= new_head[0] < 10 and 0 <= new_head[1] < 10:  # ako ne iskaca
        if new_head not in red_fields:
            if new_head not in green_fields:
                snake_fields.remove(snake_tail)
            else:
                green_fields.remove(new_head)

            if new_head not in snake_fields:
                snake_fields.append(new_head)
                new_orientation = "left" if snake_orientation == "up" else "up" if snake_orientation == "right" else "right" if snake_orientation == "down" else "down"
                new_state = (tuple(snake_fields), tuple(green_fields), tuple(red_fields), new_orientation)
                return new_state
    return state

class Snake(Problem):
    def __init__(self, initial):
        super().__init__(initial)


    @staticmethod
    def orientation_map(orientation):
        #(straight, right, left)
        if orientation == "up":#up
            return (0,1), (1,0), (-1, 0)
        elif orientation == "right":#right
            return (1,0), (0,-1), (0,1)
        elif orientation == "left":#left
            return (-1,0), (0,1), (0,-1)
        elif orientation == "down":#down
            return (0, -1), (-1, 0), (1, 0)
        return ()

    def successor(self, state):
        successors=dict()
        # state=(snake,green,red,orientation)

        s_state=continueStraight(state)
        if s_state != state:
            successors["ProdolzhiPravo"] = s_state
        l_state=turnLeft(state)
        if l_state != state:
            successors["SvrtiLevo"] = l_state
        r_state=turnRight(state)
        if r_state != state:
            successors["SvrtiDesno"] = r_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()
    def result(self, state, action):
        return self.successor(state)[action]
    def goal_test(self, state):
        return len(state[1])==0

if __name__ == '__main__':
    msnake=((0,9),(0,8),(0,7))#snake head is the last insert
    mgreen=[]
    mred=[]
    num_green=int(input())
    while num_green != 0:
        x, y = map(int, input().split(","))
        mgreen.append((x, y))
        num_green-=1
    num_red=int(input())
    while num_red != 0:
        x, y = map(int, input().split(","))
        mred.append((x, y))
        num_red-=1

    #mgreen= ((3,7) ,(4,7) ,(5,7) ,(5,5) ,(3,5) ,(3,9))
    #mred=(( 3, 8),( 4, 6),( 0, 6),( 1, 6),( 2, 6))
    morientation = "down"

    """state=(snake,green,red,orientation)
                =(((s1x,s1y), (s2x,s2y),..), ((g1x,g1y), (g2x,g2y),..), ((r1x,r1y), (r2x,r2y),..), ((str,str),(left,left), (right, right)))"""
    problem = Snake((msnake, tuple(mgreen), tuple(mred), morientation))
    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No solution found!")