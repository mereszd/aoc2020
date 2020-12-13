from sympy.ntheory.modular import crt


with open("13_input.txt", "r") as f:
    t_ = int(f.readline())
    bus_ids = []
    temp_ = f.readline().split(',')
    for t in range(len(temp_)):
        if temp_[t] != "x":
            bus_ids.append([t, int(temp_[t])])

ids = []
times = []
for bus_id in bus_ids:
    ids.append(bus_id[1])
    times.append(bus_id[1] - bus_id[0])

print(crt(ids, times)[0])