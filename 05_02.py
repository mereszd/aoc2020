boarding_passes = []
occupied_seats = []
occupied_seat_ids = []

def get_seat_id(boarding_pass):
    row_code = boarding_pass[:7]
    seat_code = boarding_pass[-3:]
    row_binary = 0b0000000
    seat_binary = 0b000
    row_value = 64
    seat_value = 4
    for x in row_code:
        if x == 'B':
            row_binary = row_binary | row_value
        row_value = row_value//2
    for y in seat_code:
        if y == 'R':
            seat_binary = seat_binary | seat_value
        seat_value = seat_value//2
    return row_binary*8+seat_binary


with open("05_input.txt", "r") as f:
    for x in f:
        boarding_passes.append(x.rstrip())

for boarding_pass in boarding_passes:
    occupied_seat_ids.append(get_seat_id(boarding_pass))

occupied_seat_ids.sort()

for occupied_seat_id in range(max(occupied_seat_ids)):
    if occupied_seat_id not in occupied_seat_ids and \
            occupied_seat_id-1 in occupied_seat_ids and occupied_seat_id+1 in occupied_seat_ids:
        print(occupied_seat_id)
