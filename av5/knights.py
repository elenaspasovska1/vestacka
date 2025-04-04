from constraint import *

def not_attacking(k1, k2):
    if abs(k1[0]-k2[0])== abs(k1[1]-k2[1]):
        return False
    return True

if __name__ == '__main__':
    problem = Problem()
    domain=[(i,j) for i in range(8) for j in range(8)]
    knights=range(8)
    problem.addVariables(knights, domain)

    for i in knights:
        for j in knights:
            if i < j:
                problem.addConstraint(not_attacking,(i,j))

    solution = problem.getSolution()
    print(solution)
