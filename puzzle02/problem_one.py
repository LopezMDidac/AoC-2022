from data import test_data, all_data
from rules import Rock, Paper, Scissors, Shape, elve_moves

## PART 1

my_moves = {
    "X": Rock(),
    "Y": Paper(),
    "Z": Scissors()
}

total_score = 0
for i in all_data:
    game = i.split(" ")
    my_move:Shape = my_moves[game[1]]
    opponent_move = elve_moves[game[0]]
    game_score = my_move == opponent_move
    total_score += my_move.score + game_score.value

print(total_score)
