def find_differences(adapters):
    built_in = max(adapters) + 3
    current_jolt = 0
    diffs = {1: 0, 2: 0, 3: 0}
    while len(adapters) != 0:
        diff = min(adapters) - current_jolt
        diffs[diff] += 1
        current_jolt = min(adapters)
        adapters.remove(min(adapters))
    diff = built_in - current_jolt
    diffs[diff] += 1
    return diffs[1]*diffs[3]


with open("10_input.txt", "r") as f:
    adapters = []
    for x in f:
        adapters.append(int(x.rstrip()))

print(find_differences(adapters.copy()))