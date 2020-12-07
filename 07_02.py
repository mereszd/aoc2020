rules = []
bags_split = {}
bags_checked = []


def containers(required_bag):
    for bag in bags_split:
        if required_bag in bag[1]:
            if bag[0] not in bags_checked:
                bags_checked.append(bag[0])
                containers(bag[0])

def cost(current_bag):
    contains = 0
    for bag_within in bags_split[current_bag]:
        contains += bag_within[0] + bag_within[0] * cost(bag_within[1])
    return contains


with open("07_input.txt", "r") as f:
    for x in f:
        rules.append(x.rstrip())

for rule in rules:
    x, y = rule.split('contain')
    contains = y.split(',')
    x = x[:-2]
    bags_split[x] = []
    for bag in contains:
        temp_ = []
        if bag[1] != 'n':
            temp_.append(int(bag[1]))
            if bag[1] == '1':
                temp_.append(bag.strip('.')[3:])
            else:
                temp_.append(bag.strip('.')[3:-1])
            bags_split[x].append(temp_)

print(cost('shiny gold bag'))