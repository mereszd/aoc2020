answers = []
group_answers = []

with open("06_input.txt", "r") as f:
    for x in f:
        if x != '\n':
            person = []
            for char in x:
                if char != '\n':
                    person.append(char)
            group_answers.append(person)
        else:
            answers.append(group_answers)
            group_answers = []
    answers.append(group_answers)


total_yes = 0
for group in answers:
    intersect = set(group[0])
    for person in group:
        intersect = intersect & set(person)
    total_yes += len(intersect)

print(total_yes)
