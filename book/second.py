from constraint import *


def is_not_overlapping(time1, time2):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    time_slots = {
        "10": 10,
        "11": 11,
        "12": 12,
        "13": 13,
        "14": 14,
        "15": 15,
    }

    # Разделување на ден и час
    day1, hour1 = time1.split("_")
    day2, hour2 = time2.split("_")

    # Проверка ако деновите се различни
    if day1 != day2:
        return True

    # Проверка ако термини се различни барем 2 часа
    if abs(time_slots[hour1] - time_slots[hour2]) >= 2:
        return True

    return False
def not_repeating():
    pass
"""broj na termini za sekoj predmet od vlex
    broj za termini na vezbi se sekogas 1 akopredmetot ima vezzbi
    eden termin trae 2 casa"""
if __name__=='__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R =  int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    for i in range(casovi_AI):
        problem.addVariable("AI_cas"+str(i+1), AI_predavanja_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    for i in range(casovi_ML):
        problem.addVariable("ML_cas"+str(i+1), ML_predavanja_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    for i in range(casovi_R):
        problem.addVariable("R_cas"+str(i+1), R_predavanja_domain)
    for i in range(casovi_BI):
        problem.addVariable("BI_cas"+str(i+1), BI_predavanja_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    """constraints
    bez preklopuvanje"""
    for va1 in problem._variables:
        for va2 in problem._variables:
            if va1!=va2:
                problem.addConstraint(is_not_overlapping,(va1,va2))
    """
    predavanjata i vezbite za ml mora da pocnuvaat vo razlicno vreme
    """
    problem.addConstraint(AllDifferentConstraint(), ["ML_cas" + str(i + 1) for i in range(casovi_ML)]+["ML_vezbi"])
    solution = problem.getSolution()

    print(solution)
