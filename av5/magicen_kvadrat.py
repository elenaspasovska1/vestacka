from constraint import *

if __name__ == '__main__':
    problem = Problem()
    domain= range(1,17)
    var = range(0,16)

    problem.addVariables(var, domain)

    problem.addConstraint(AllDifferentConstraint(), var)

    """0  1  2  3
       4  5  6  7
       8  9  10 11
       12 13 14 15"""

    for row in range(4):
        problem.addConstraint(ExactSumConstraint(34),[row*4+i for i in range(4)])

    for column in range(4):
        problem.addConstraint(ExactSumConstraint(34),[column + 4*i for i in range(4)])

    problem.addConstraint(ExactSumConstraint(34),range(0,16,5))
    problem.addConstraint(ExactSumConstraint(34),range(3,13,3))

    solution = problem.getSolution()
    print(solution)
