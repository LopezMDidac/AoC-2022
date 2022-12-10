from enum import Enum

class Direction(Enum):
    U = "UP"
    D = "DOWN"
    L = "LEFT"
    R = "RIGHT"

class MapPosition:

    def __init__(self, n_knots):
        self.knots = [[0,0] for _ in range(n_knots)]
        self.T_positions = [self.knots[-1].copy()]


    def move(self, dir:Direction):
        self.move_head(dir)
        for i in range(1, len(self.knots)):
            if self.knot_should_move(self.knots[i-1], self.knots[i]):
                if self.knots[i][0] > self.knots[i-1][0]:
                    self.knots[i][0] -= 1
                elif self.knots[i][0] < self.knots[i-1][0]:
                    self.knots[i][0] += 1
                if self.knots[i][1] > self.knots[i-1][1]:
                    self.knots[i][1] -= 1
                elif self.knots[i][1] < self.knots[i-1][1]:
                    self.knots[i][1] += 1
                if i == len(self.knots)-1 and self.knots[i] not in self.T_positions:
                    self.T_positions.append(self.knots[i].copy())
            else:
                break

    def knot_should_move(self, head_knot, tail_knot):
        return abs(head_knot[0] - tail_knot[0]) > 1 or abs(head_knot[1] - tail_knot[1]) > 1
    
    def move_head(self, dir:Direction):
        if dir is Direction.U:
            self.knots[0][0] +=1
        elif dir is Direction.D:
            self.knots[0][0] -=1
        elif dir is Direction.L:
            self.knots[0][1] -=1
        else:
            self.knots[0][1] +=1