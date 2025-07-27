from stable_matching import stable_matching

men_preferences = [
    [0, 1, 2],
    [2, 1, 0],
    [1, 2, 0]
]

women_preferences = [
    [2, 1, 0],
    [0, 1, 2],
    [0, 1, 2]
]

result = stable_matching(men_preferences, women_preferences)
print("Stable Matches (man, woman):", result)
