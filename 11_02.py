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
                vis_seat = seat - 1
                vis_row = row - 1
                while vis_seat >= 0 and vis_row >= 0:
                    if current_sp[vis_row][vis_seat] == '#':
                        occ_count += 1
                        break
                    elif current_sp[vis_row][vis_seat] == 'L':
                        break
                    else:
                        vis_row -= 1
                        vis_seat -= 1
                # Top
                vis_seat = seat
                vis_row = row - 1
                while vis_row >= 0:
                    if current_sp[vis_row][vis_seat] == '#':
                        occ_count += 1
                        break
                    elif current_sp[vis_row][vis_seat] == 'L':
                        break
                    else:
                        vis_row -= 1
                # Top Right
                vis_seat = seat + 1
                vis_row = row - 1
                while vis_row >= 0 and vis_seat < len(rows[row]):
                    if current_sp[vis_row][vis_seat] == '#':
                        occ_count += 1
                        break
                    elif current_sp[vis_row][vis_seat] == 'L':
                        break
                    else:
                        vis_seat += 1
                        vis_row -= 1
                # Left
                vis_seat = seat - 1
                vis_row = row
                while vis_seat >= 0:
                    if current_sp[vis_row][vis_seat] == '#':
                        occ_count += 1
                        break
                    elif current_sp[vis_row][vis_seat] == 'L':
                        break
                    else:
                        vis_seat -= 1
                # Right
                vis_seat = seat + 1
                vis_row = row
                while vis_seat < len(rows[row]):
                    if current_sp[vis_row][vis_seat] == '#':
                        occ_count += 1
                        break
                    elif current_sp[vis_row][vis_seat] == 'L':
                        break
                    else:
                        vis_seat += 1
                # Bottom Left
                vis_seat = seat - 1
                vis_row = row + 1
                while vis_seat >= 0 and vis_row < len(rows):
                    if current_sp[vis_row][vis_seat] == '#':
                        occ_count += 1
                        break
                    elif current_sp[vis_row][vis_seat] == 'L':
                        break
                    else:
                        vis_row += 1
                        vis_seat -= 1
                # Bottom
                vis_seat = seat
                vis_row = row + 1
                while vis_row < len(rows):
                    if current_sp[vis_row][vis_seat] == '#':
                        occ_count += 1
                        break
                    elif current_sp[vis_row][vis_seat] == 'L':
                        break
                    else:
                        vis_row += 1
                # Bottom Right
                vis_seat = seat + 1
                vis_row = row + 1
                while vis_seat < len(rows[row]) and vis_row < len(rows):
                    if current_sp[vis_row][vis_seat] == '#':
                        occ_count += 1
                        break
                    elif current_sp[vis_row][vis_seat] == 'L':
                        break
                    else:
                        vis_row += 1
                        vis_seat += 1
                # Calculate next occupancy
                if current_sp[row][seat] == 'L':
                    if occ_count == 0:
                        new_row += '#'
                    else:
                        new_row += 'L'
                elif current_sp[row][seat] == '#':
                    if occ_count >= 5:
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
