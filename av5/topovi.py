from constraint import *

def not_attacking(r1,r2):
    return r1[0] != r2[0] and r1[1] != r2[1]
"""
if __name__ == '__main__':
    problem = Problem()
    domain=[(i,j) for i in range(1,10) for j in range(1,10)]

    rooks=range(1,9)
    problem.addVariables(rooks, domain)

    for rook1 in rooks:
        for rook2 in rooks:
            if rook1 != rook2:
                problem.addConstraint(not_attacking,(rook1,rook2))

    solution = problem.getSolution()
    print(solution)"""

if __name__ == '__main__':
    problem = Problem()
    rooks= range(0,8)
    domain=range(0,8)

    problem.addVariables(rooks, domain)

    problem.addConstraint(AllDifferentConstraint(), rooks)

    solution = problem.getSolution()
    print(solution)