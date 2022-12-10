from rules import MapPosition, Direction
from data import test_data, all_data

moves = all_data


## PART 1
knots = 2
map_pos = MapPosition(knots)

for move in moves:
    dir, n = move.split(" ")
    n=int(n)
    while n > 0:
        map_pos.move(Direction[dir])
        n-=1

print(len(map_pos.T_positions))

    
## PART 2
knots = 10
map_pos = MapPosition(knots)

for move in moves:
    dir, n = move.split(" ")
    n=int(n)
    while n > 0:
        map_pos.move(Direction[dir])
        n-=1

print(len(map_pos.T_positions))