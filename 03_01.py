biomes = []

def check_trees (column_increment, row_increment):
    row_increment -= 1
    current_column = 0
    trees_hit = 0
    biomes_iter = iter(range(len(biomes)))
    for i in biomes_iter:
        print(i)
        if biomes[i][current_column%len(biomes[i])] == "#":
            trees_hit += 1
        current_column += column_increment
        for j in range(row_increment):
            next(biomes_iter, None)
    return trees_hit


with open("03_input.txt", "r") as f:
    for x in f:
        biomes.append(x.rstrip())

total_trees = check_trees(1, 1)
total_trees *= check_trees(3, 1)
total_trees *= check_trees(5, 1)
total_trees *= check_trees(7, 1)
total_trees *= check_trees(1, 2)

print(total_trees)