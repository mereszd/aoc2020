# starting = [0, 3, 6]
starting = [7, 14, 0, 17, 11, 1, 2]

spoken = []
last_time = {}
target = 30000000
previous = 0

# Adding False to index 0, so index corresponds to turns
spoken.append(False)

for i in range(len(starting)):
    spoken.append(starting[i])
    last_time[starting[i]] = [i+1]
    previous = starting[i]

for i in range(len(starting) + 1, target + 1):
    # First or second time spoken
    if previous not in last_time.keys() or len(last_time[previous]) == 1:
        to_add = 0
        # print("Turn {}, {} wasn't spoken twice before. Appending {}".format(i, previous, 0))
    else:
        to_add = last_time[previous][1] - last_time[previous][0]
        # print("Turn {}, {} was spoken before at turns {} and {} recently. Appending {}".format(i, previous, last_time[previous][1], last_time[previous][0], to_add))
    if to_add in last_time.keys():
        if len(last_time[to_add]) == 1:
            last_time[to_add].append(i)
        else:
            last_time[to_add][0] = last_time[to_add][1]
            last_time[to_add][1] = i
    else:
        last_time[to_add] = [i]
    previous = to_add

print(previous)