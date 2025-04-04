from searching_framework import Problem, astar_search


# Movement functions remain the same.
def akcija_gore(coveceQ, broj_skokanja=1):
    return (coveceQ[0], coveceQ[1] + broj_skokanja)


def akcija_gore_desno(coveceQ, broj_skokanja=1):
    return (coveceQ[0] + broj_skokanja, coveceQ[1] + broj_skokanja)


def akcija_gore_levo(coveceQ, broj_skokanja=1):
    return (coveceQ[0] - broj_skokanja, coveceQ[1] + broj_skokanja)


def akcija_stoj(coveceQ):
    return coveceQ


def is_possible_move(covece, allowed, goal):
    # Check grid boundaries
    if covece[0] < 0 or covece[0] > 4 or covece[1] < 0 or covece[1] > 8:
        return False
    # Allow the move if it lands on an allowed cell or reaches the dynamic goal.
    if covece == goal or covece in allowed:
        return True
    return False


def moves(funk, covece):
    if funk == 'Stoj':
        return akcija_stoj(covece)
    elif funk == 'Gore 1':
        return akcija_gore(covece)
    elif funk == 'Gore 2':
        return akcija_gore(covece, 2)
    elif funk == 'Gore-desno 1':
        return akcija_gore_desno(covece)
    elif funk == 'Gore-desno 2':
        return akcija_gore_desno(covece, 2)
    elif funk == 'Gore-levo 1':
        return akcija_gore_levo(covece)
    elif funk == 'Gore-levo 2':
        return akcija_gore_levo(covece, 2)


class Istrazuvac(Problem):
    def __init__(self, initial, goal, heksagoni, nasokaa):
        # self.goal stores the base goal. We'll compute a dynamic goal from it.
        super().__init__(initial, goal)
        self.heksagoni = heksagoni
        self.nasokaa = nasokaa

    def compute_dynamic_goal(self):
        # Compute a dynamic goal based on the current nasokaa.
        goal_x, goal_y = self.goal
        if self.nasokaa == 'desno':
            dynamic_goal = (goal_x + 1, goal_y)
        else:
            dynamic_goal = (goal_x - 1, goal_y)
        return dynamic_goal

    def successor(self, state):
        successors = {}
        # Keep the current state of the man.
        covece = state
        funkcii = ['Stoj', 'Gore 1', 'Gore 2',
                   'Gore-desno 1', 'Gore-desno 2',
                   'Gore-levo 1', 'Gore-levo 2']
        dynamic_goal = self.compute_dynamic_goal()

        for move in funkcii:
            new_state = moves(move, covece)
            if is_possible_move(new_state, self.heksagoni, dynamic_goal):
                successors[move] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        # Use the same dynamic goal for testing as for move validation.
        dynamic_goal = self.compute_dynamic_goal()
        return state == dynamic_goal

    def h(self, node):
        # Use Manhattan distance to dynamic goal, scaled down.
        dynamic_goal = self.compute_dynamic_goal()
        return (abs(node.state[0] - dynamic_goal[0]) + abs(node.state[1] - dynamic_goal[1])) / 3


if __name__ == '__main__':
    # Allowed positions as in your code.
    allowed = [(1, 0), (2, 0), (3, 0),
               (1, 1), (2, 1),
               (0, 2), (2, 2), (4, 2),
               (1, 3), (3, 3), (4, 3),
               (0, 4), (2, 4),
               (2, 5), (3, 5),
               (0, 6), (2, 6),
               (1, 7), (3, 7)]

    tmp = input().strip().split(',')
    covece_pos = (int(tmp[0]), int(tmp[1]))
    tmp = input().strip().split(',')
    kukja_pos = (int(tmp[0]), int(tmp[1]))
    nasoka = input().strip()

    istrazuvac = Istrazuvac(covece_pos, kukja_pos, allowed, nasoka)
    result = astar_search(istrazuvac)
    if result is not None:
        print(result.solution())
    else:
        print("No solution!")
