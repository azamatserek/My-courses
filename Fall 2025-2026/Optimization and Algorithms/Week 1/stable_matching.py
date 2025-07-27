def stable_matching(men_preferences, women_preferences):
    n = len(men_preferences)

    # All men and women are initially free
    free_men = list(range(n))

    # Keep track of the current engagement of women
    women_partner = [None] * n

    # Index of the next woman to propose to for each man
    men_next_proposal = [0] * n

    # Invert women preferences for fast comparison
    women_rankings = []
    for preferences in women_preferences:
        rank = {man: i for i, man in enumerate(preferences)}
        women_rankings.append(rank)

    while free_men:
        man = free_men[0]
        # Get the highest-ranked woman not yet proposed to
        woman_index = men_preferences[man][men_next_proposal[man]]
        men_next_proposal[man] += 1

        current_partner = women_partner[woman_index]

        # If woman is free, accept proposal
        if current_partner is None:
            women_partner[woman_index] = man
            free_men.pop(0)
        else:
            # Check if she prefers the new man
            if women_rankings[woman_index][man] < women_rankings[woman_index][current_partner]:
                women_partner[woman_index] = man
                free_men.pop(0)
                free_men.append(current_partner)

    # Return list of (man, woman) pairs
    matching = []
    for woman_index, man in enumerate(women_partner):
        matching.append((man, woman_index))

    return matching
