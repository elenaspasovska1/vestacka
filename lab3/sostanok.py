from constraint import Problem, BacktrackingSolver


def valid_meeting_time(simona, marija, petar):
    """Ensure Simona is always present and at least one more person attends."""
    return simona == 1 and (marija == 1 or petar == 1)


def is_available(time, person_times):
    return time in person_times


def check_marija_availability(time, marija):
    return marija == 1 if is_available(time, {14, 15, 18}) else marija == 0


def check_petar_availability(time, petar):
    return petar == 1 if is_available(time, {12, 13, 16, 17, 18, 19}) else petar == 0


def check_simona_availability(time):
    return is_available(time, {13, 14, 16, 19})


if __name__ == "__main__":
    problem = Problem(BacktrackingSolver())

    available_times = sorted({13, 14, 16, 19} | {14, 15, 18} | {12, 13, 16, 17, 18, 19})

    problem.addVariable("Simona_prisustvo", [1])  # Simona must be present
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", available_times)

    problem.addConstraint(valid_meeting_time, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])
    problem.addConstraint(check_simona_availability, ["vreme_sostanok"])
    problem.addConstraint(check_marija_availability, ["vreme_sostanok", "Marija_prisustvo"])
    problem.addConstraint(check_petar_availability, ["vreme_sostanok", "Petar_prisustvo"])


    solutions = problem.getSolutions()
    for solution in solutions:
        print(f"{{'Simona_prisustvo': {solution['Simona_prisustvo']}, 'Marija_prisustvo': {solution['Marija_prisustvo']}, 'Petar_prisustvo': {solution['Petar_prisustvo']}, 'vreme_sostanok': {solution['vreme_sostanok']}}}")

