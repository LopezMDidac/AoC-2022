from data import test_data, all_data
from rules import ResolutionScore, Shape, elve_moves

## PART 2

expected_resolution = {
    "X": ResolutionScore.LOSE,
    "Y": ResolutionScore.DRAW,
    "Z": ResolutionScore.WIN
}

total_score = 0
for i in all_data:
    game = i.split(" ")
    opponent_move:Shape = elve_moves[game[0]]
    game_resolution = expected_resolution[game[1]]
    my_move = opponent_move.get_opponent_shape_to(game_resolution)
    game_score = game_resolution.value + my_move.score
    total_score += game_score

print(total_score)