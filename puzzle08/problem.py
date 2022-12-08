from data import test_data, all_data


data = all_data
visible_trees = len(data)*2 + len(data[0])*2 - 4
# print(visible_trees)

def tree_is_visible(i,j):
    top = [data[k][j] for k in range(i)]
    bot = [data[k][j] for k in range(i+1, len(data))]
    left = [data[i][k] for k in range(j)]
    right = [data[i][k] for k in range(j+1, len(data[i]))]
    tree = data[i][j]
    return tree > max(top) or tree > max(bot) or tree > max(left) or tree > max(right)

def tree_visibility(trees, tree):
    visibility = 0
    for t in trees:
        if tree > t:
            visibility +=1
        else:
            visibility +=1
            break

    return visibility


def tree_scenic_score(i,j):
    tree = data[i][j]

    top = [data[k][j] for k in range(i-1,-1, -1)]
    bot = [data[k][j] for k in range(i+1, len(data))]
    left = [data[i][k] for k in range(j-1, -1, -1)]
    right = [data[i][k] for k in range(j+1, len(data[i]))]

    top_visibility =  tree_visibility(top, tree)
    bot_visibility =  tree_visibility(bot, tree)
    left_visibility = tree_visibility(left, tree)
    right_visibility= tree_visibility(right, tree)

    return top_visibility * bot_visibility * left_visibility * right_visibility

# print(tree_scenic_score(3,2))
# for i in range(1, len(data)-1):
#     for j in range(1, len(data[i])-1):
#         if tree_is_visible(i,j):
#             visible_trees +=1
        
# print(visible_trees)


scenic_score = 0
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        score = tree_scenic_score(i,j)
        scenic_score = max(score, scenic_score)
        

print(scenic_score)