def find_differences(adapters):
    paths = [0] * len(adapters)
    paths[0] = paths[1] = 1

    if adapters[2] - adapters[0] <= 3:
        paths[2] = 2
    else:
        paths[2] = 1

    for i in range(3, len(adapters)):
        for j in range(1, 4):
            if adapters[i] - adapters[i-j] <= 3:
                paths[i] += paths[i-j]

    return paths[-1]


with open("10_input.txt", "r") as f:
    adapters = []
    for x in f:
        adapters.append(int(x.rstrip()))

adapters.append(0)
adapters.append(max(adapters) + 3)
adapters.sort()

print(find_differences(adapters.copy()))