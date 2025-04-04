from constraint import Problem, BacktrackingSolver, MaxSumConstraint

if __name__ == "__main__":
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Define problem
    problem = Problem(BacktrackingSolver())

    # Define domain (available time slots)
    domain = [f'T{i + 1}' for i in range(num)]

    # Define variables
    problem.addVariables(papers.keys(), domain)

    # Constraints
    # Each session can have at most 4 papers
    for term in domain:
        problem.addConstraint(MaxSumConstraint(4), [paper for paper in papers.keys()])

    # Papers from the same topic should be in the same term if they fit
    topics = {}
    for paper, topic in papers.items():
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(paper)

    for topic_papers in topics.values():
        if len(topic_papers) <= 4:
            problem.addConstraint(lambda *args: len(set(args)) == 1, topic_papers)

    # Get solution
    result = problem.getSolution()

    # Print result
    for paper, term in result.items():
        print(f"{paper}: {term}")