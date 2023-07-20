import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:


player_scores = {
    players_dict["name"]: len(
        [score for score in players_dict["numbers"] if score in lottery_numbers]
    )
    for players_dict in players
}

check_score = -1
winner = ""
for player, score in player_scores.items():
    if score > check_score:
        check_score = score
        winner = player


print(f"{winner} has won {100**check_score}.")
# 100 ** len(numbers_matched)
