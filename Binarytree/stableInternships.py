

def stableInternships(interns, teams):
    chosenInterns = {}
    freeInterns = list(range(len(interns)))
    currentInternChoices = [0] * len(interns)
    teamMap = []
    for team in teams:
        rank = {}
        for i, intern in enumerate(team):
            rank[intern] = i
        teamMap.append(rank)

    while len(freeInterns) > 0:
        intern = freeInterns.pop()
        internChoices = interns[intern]
        teamPreference = internChoices[currentInternChoices[intern]]
        currentInternChoices[intern] += 1

        if teamPreference not in chosenInterns:
            chosenInterns[teamPreference] = intern
            continue
        previousIntern = chosenInterns[teamPreference]
        previousInternRank = teamMap[teamPreference][previousIntern]
        currentInternRank = teamMap[teamPreference][intern]
        if currentInternRank < previousInternRank:
            freeInterns.append(previousIntern)
            chosenInterns[teamPreference] = intern
        else:
            freeInterns.append(intern)

    return [[intern, team] for team, intern in chosenInterns.items()]


interns = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 2, 0]
]
teams = [
    [2, 1, 0],
    [0, 1, 2],
    [0, 1, 2]
]

internsAndTeams = stableInternships(interns, teams)
print(internsAndTeams)
