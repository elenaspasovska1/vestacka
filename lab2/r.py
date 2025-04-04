from searching_framework import Problem, astar_search

vlezovi = {
    'gore': (0, 1),
    'dolu': (0, -1),
    'levo': (-1, 0),
    'desno': (1, 0)
}

def akcija_gore(coveceQ, broj_skokanja=1):
    new_state = (coveceQ[0], coveceQ[1] + broj_skokanja)
    return new_state


def akcija_gore_desno(coveceQ, broj_skokanja=1):
    new_state = (coveceQ[0] + broj_skokanja,
                 coveceQ[1] + broj_skokanja)
    return new_state


def akcija_gore_levo(coveceQ, broj_skokanja=1):
    new_state = (coveceQ[0] - broj_skokanja,
                 coveceQ[1] + broj_skokanja)
    return new_state

def akcija_stoj(coveceQ):
    return coveceQ


def is_possible_move(covece, allowed, goal):
    if covece[0] < 0 or 4 < covece[0] or covece[1] < 0 or 8 < covece[1]:
        return False
    if covece == goal:
        return True
    if covece in allowed:
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
        super().__init__(initial, goal)
        self.heksagoni = heksagoni
        self.nasokaa = nasokaa

    def successor(self, state):
        successors = {}
        covece = state
        funkcii = ['Stoj', 'Gore 1', 'Gore 2', 'Gore-desno 1', 'Gore-desno 2', 'Gore-levo 1', 'Gore-levo 2']

        tmp_goll = self.goal
        goal_x, goal_y = tmp_goll

        if self.nasokaa == 'desno':
            tmp_goll = (goal_x + 1, goal_y)
        else:
            tmp_goll = (goal_x - 1, goal_y)

        if tmp_goll[0] == 4:
            self.nasokaa = 'levo'
        elif tmp_goll[0] == 0:
            self.nasokaa = 'desno'


        for i in funkcii:
            tmp = moves(i, covece)
            if is_possible_move(tmp, self.heksagoni, self.goal):
                successors[i] = tmp

        # if is_possible_move(covece, self.heksagoni, self.goal):
        #     successors[funkcii[0]] = covece
        #
        # if is_possible_move(akcija_gore(covece), self.heksagoni, self.goal):
        #     successors[funkcii[1]] = akcija_gore(covece)
        #
        # if is_possible_move(akcija_gore(covece, 2), self.heksagoni, self.goal):
        #     successors[funkcii[2]] = akcija_gore(covece, 2)
        #
        # if is_possible_move(akcija_gore_desno(covece), self.heksagoni, self.goal):
        #     successors[funkcii[3]] = akcija_gore_desno(covece)
        #
        # if is_possible_move(akcija_gore_desno(covece, 2), self.heksagoni, self.goal):
        #     successors[funkcii[4]] = akcija_gore_desno(covece, 2)
        #
        # if is_possible_move(akcija_gore_levo(covece), self.heksagoni, self.goal):
        #     successors[funkcii[5]] = akcija_gore_levo(covece)
        #
        # if is_possible_move(akcija_gore_levo(covece, 2), self.heksagoni, self.goal):
        #     successors[funkcii[6]] = akcija_gore_levo(covece, 2)


        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal

    def h(self, node):
        return (abs(node.state[0] - self.goal[0]) + abs(
            node.state[1] - self.goal[1]))/3


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    tmp = input().strip().split(',')
    covece_pos = (int(tmp[0]), int(tmp[1]))
    tmp = input().strip().split(',')
    kukja_pos = (int(tmp[0]), int(tmp[1]))
    nasoka = input().strip()

    istrazuvac = Istrazuvac(covece_pos, kukja_pos, allowed, nasoka)

    result = astar_search(istrazuvac)
    if result is not None:
        print(result.solution())


