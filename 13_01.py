with open("13_input.txt", "r") as f:
    depart_time = int(f.readline())
    bus_ids = []
    temp_ = f.readline().split(',')
    for t in temp_:
        if t != "x":
            bus_ids.append(int(t))

timetable = {}
for bus_id in bus_ids:
    n = depart_time // bus_id
    if depart_time % bus_id == 0:
        timetable[bus_id] = n
    else:
        timetable[bus_id] = bus_id * (n+1)

shortest_wait = [depart_time, 0]
for time_id in timetable.keys():
    wait_time = timetable[time_id] - depart_time
    if wait_time < shortest_wait[0]:
        shortest_wait = [wait_time, time_id]

print(shortest_wait[0] * shortest_wait[1])