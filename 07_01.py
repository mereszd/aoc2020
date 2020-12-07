rules = []
bags_split = []
bags_checked = []


def containers(required_bag):
    for bag in bags_split:
        if required_bag in bag[1]:
            if bag[0] not in bags_checked:
                bags_checked.append(bag[0])
                containers(bag[0])


with open("07_input.txt", "r") as f:
    for x in f:
        rules.append(x.rstrip())

for rule in rules:
    x, y = rule.split('contain')
    x = x[:-2]
    bags_split.append([x, y])

containers('shiny gold bag')
print(len(bags_checked))
print(bags_checked)