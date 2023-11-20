# open input files
with open('exampleinput.txt', 'r') as exampleinputfile:
    exampleinput = exampleinputfile.read()
with open('input.txt', 'r') as inputfile:
    input = inputfile.read()


# -------------------------------------------------------------------------------------------------------------
# Part 1

# format input into two separate lists; rows and columns
rowslist = input.splitlines()
column = ''
columnslist = []
for x in range(len(rowslist[0])):
    for row in rowslist:
        column += row[x]
    columnslist.append(column)
    column = ''

# a larger tree than the original is always indicating lack of visibility from that direction
# row count is column index
# column count is row index

# determine a single tree's visibility status
def tree_visibility(row,column):
    tree = rowslist[row][column]
    visible_to_the_east = all(int(tree) > int(othertree) for othertree in rowslist[row][column + 1:])
    visible_to_the_west = all(int(tree) > int(othertree) for othertree in rowslist[row][:column])
    visible_to_the_north = all(int(tree) > int(othertree) for othertree in columnslist[column][:row])
    visible_to_the_south = all(int(tree) > int(othertree) for othertree in columnslist[column][row + 1:])
    visible = any([visible_to_the_east,visible_to_the_west,visible_to_the_north,visible_to_the_south])
    return visible

# iterate through input using tree visibility function
def tree_iteration(input):
    visiblecount = 0
    for rowcount, row in enumerate(rowslist):
        for columncount, tree in enumerate(row):
            if tree_visibility(rowcount,columncount) == True:
                visiblecount += 1
    return visiblecount


# -------------------------------------------------------------------------------------------------------------
# Part 2

# determine a single tree's, single direction vision
def directional_scenic_score(tree,tree_list):
    count = 0
    index = 0
    while index != len(tree_list):
        count += 1
        if int(tree_list[index]) >= int(tree):
            return count
        index += 1
    return count

# determine a single tree's scenic score
def trees_scenic_score(row,column):
    westreversedlist = list(reversed(rowslist[row][:column]))
    northreversedlist = list(reversed(columnslist[column][:row]))
    tree = rowslist[row][column]
    vision_to_the_east = directional_scenic_score(tree,rowslist[row][column + 1:])
    vision_to_the_west = directional_scenic_score(tree,westreversedlist)
    vision_to_the_north = directional_scenic_score(tree,northreversedlist)
    vision_to_the_south = directional_scenic_score(tree,columnslist[column][row + 1:])
    scenicscore = vision_to_the_east * vision_to_the_west * vision_to_the_north * vision_to_the_south
    return scenicscore

# iterate through input using trees scenic score function
def best_scenic_score(input):
    bestscenicscore = 0
    for rowcount, row in enumerate(rowslist):
        for columncount, tree in enumerate(row):
            if trees_scenic_score(rowcount,columncount) > bestscenicscore:
                bestscenicscore = trees_scenic_score(rowcount,columncount)
    return bestscenicscore

print(best_scenic_score(input))


        

            
                
                    








    
