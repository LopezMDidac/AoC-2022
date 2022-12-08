from rules import data, tree_is_visible, visible_trees, tree_scenic_score

## PART 1
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        if tree_is_visible(i,j):
            visible_trees +=1
        
print(visible_trees)


## PART 2
scenic_score = 0
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        score = tree_scenic_score(i,j)
        scenic_score = max(score, scenic_score)
        
print(scenic_score)