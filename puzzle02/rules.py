from enum import Enum

class ResolutionScore(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

class Shape:
    score: int

    def __init__(self, win_against, lose_against):
        self.win_against = win_against
        self.lose_against = lose_against
        
    def __eq__(self, other):
        if isinstance(other, self.win_against):
            return ResolutionScore.WIN
        elif isinstance(other, self.lose_against):
            return ResolutionScore.LOSE
        return ResolutionScore.DRAW
    
    def get_opponent_shape_to(self, result: ResolutionScore):
        if result is result.DRAW:
            return type(self)
        elif result is result.WIN:
            return self.lose_against
        return self.win_against

class Rock(Shape):
    score = 1
    def __init__(self):
        super().__init__(Scissors, Paper)

class Paper(Shape):
    score = 2

    def __init__(self):
        super().__init__(Rock, Scissors)


class Scissors(Shape):
    score = 3

    def __init__(self):
        super().__init__(Paper, Rock)

elve_moves = {
    "A": Rock(),
    "B": Paper(),
    "C": Scissors()
}