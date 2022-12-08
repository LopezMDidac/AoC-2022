from collections import deque
from re import findall
from data import test_data_initial, test_data_moves
from data import all_data_initial, all_data_moves



data = zip(*all_data_initial)
stacks = list[deque]()

for stack in data:
    stacks.append(deque([crate[1] for crate in stack if not crate.isspace()]))

## PART 1
for move in all_data_moves:
    n, orig, dest =  (int(s) for s in findall("\d+", move))
    while n > 0:
        crate = stacks[orig-1].popleft()
        stacks[dest-1].appendleft(crate)
        n-=1

result = "".join([stack.popleft() for stack in stacks])
print(result)

## PART 2

for move in all_data_moves:
    n, orig, dest =  (int(s) for s in findall("\d+", move))
    
    crates = [stacks[orig-1].popleft() for i in range(n)]
    [stacks[dest-1].appendleft(crate) for crate in crates[::-1]]


result = "".join([stack.popleft() for stack in stacks])
print(result)


