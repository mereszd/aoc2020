def ticket_error(fields, nearby_ticket):
    for value in nearby_ticket:
        valid = False
        for field in fields:
            if fields[field][0][0] <= value <= fields[field][0][1] or fields[field][1][0] <= value <= fields[field][1][1]:
                valid = True
                break
        if valid is False:
            return False
    return True



with open("16_input.txt", "r") as f:
    fields = {}
    your_ticket = []
    nearby_tickets = []
    state = 'fields'
    for x in f:
        if x == '\n':
            continue
        elif x == 'your ticket:\n':
            state = 'your_ticket'
            continue
        elif x == 'nearby tickets:\n':
            state ='nearby_tickets'
            continue
        elif state == 'fields':
            field, values_raw = x.rstrip().split(':')
            values_split = values_raw.split(' ')
            value1 = [int(i) for i in values_split[1].split('-')]
            value2 = [int(i) for i in values_split[3].split('-')]
            fields[field] = [value1, value2]
        elif state == 'your_ticket':
            your_ticket = [int(i) for i in x.rstrip().split(',')]
        elif state == 'nearby_tickets':
            nearby_tickets.append([int(i) for i in x.rstrip().split(',')])


good_tickets = []
for nearby_ticket in nearby_tickets:
    if ticket_error(fields, nearby_ticket):
        good_tickets.append(nearby_ticket)

not_possible_fields = []
for i in range(len(fields)):
    not_possible_fields.append([])

for good_ticket in good_tickets:
    for i in range(len(good_ticket)):
        for field in fields:
            if fields[field][0][0] <= good_ticket[i] <= fields[field][0][1] or fields[field][1][0] <= good_ticket[i] <= fields[field][1][1]:
                pass
            else:
                if field not in not_possible_fields[i]:
                    not_possible_fields[i].append(field)

possible_fields = []
for i in range(len(fields)):
    possible_fields.append(list(set(fields.keys())-set(not_possible_fields[i])))

for i in range(100):
    for i in range(len(possible_fields)):
        if len(possible_fields[i]) == 1:
            only_possibility = possible_fields[i][0]
            for j in range(len(possible_fields)):
                if i != j and only_possibility in possible_fields[j]:
                    possible_fields[j].remove(only_possibility)

answer = 1
for i in range(len(possible_fields)):
    if 'departure' in possible_fields[i][0]:
        answer *= your_ticket[i]

print(answer)
