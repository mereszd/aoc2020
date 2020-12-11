import copy


def calculate_occupied(rows):
    next_round = rows
    while True:
        current_sp = next_round.copy()
        next_round = []
        for row in range(len(rows)):
            new_row = ''
            for seat in range(len(rows[row])):
                occ_count = 0
                # Top Left
                if row > 0 and seat > 0 and current_sp[row-1][seat-1] == '#':
                    occ_count += 1
                # Top
                if row > 0 and current_sp[row-1][seat] == '#':
                    occ_count += 1
                # Top Right
                if row > 0 and seat < len(rows[row])-1 and current_sp[row-1][seat+1] == '#':
                    occ_count += 1
                # Left
                if seat > 0 and current_sp[row][seat-1] == '#':
                    occ_count += 1
                # Right
                if seat < len(rows[row])-1 and current_sp[row][seat+1] == '#':
                    occ_count += 1
                # Bottom Left
                if seat > 0 and row < len(rows)-1 and current_sp[row+1][seat-1] == '#':
                    occ_count += 1
                # Bottom
                if row < len(rows)-1 and current_sp[row+1][seat] == '#':
                    occ_count += 1
                # Bottom Right
                if seat < len(rows[row])-1 and row < len(rows)-1 and current_sp[row+1][seat+1] == '#':
                    occ_count += 1
                if current_sp[row][seat] == 'L':
                    if occ_count == 0:
                        new_row += '#'
                    else:
                        new_row += 'L'
                elif current_sp[row][seat] == '#':
                    if occ_count >= 4:
                        new_row += 'L'
                    else:
                        new_row += '#'
                if current_sp[row][seat] == '.':
                    new_row += '.'
            next_round.append(new_row)
        if current_sp == next_round:
            break
    final_count = 0
    for line in current_sp:
        final_count += line.count('#')
    return current_sp, final_count


with open("11_input.txt", "r") as f:
    rows = []
    for x in f:
        rows.append(x.rstrip())

final_sp, occ_seats = calculate_occupied(rows)
for line in final_sp:
    print(line)
print(occ_seats)
