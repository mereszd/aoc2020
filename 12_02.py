def do_actions(actions):
    current_dir = 'E'
    current_pos = [0, 0]
    current_wp = [10, 1]
    for action in actions:
        if action[0] == 'L':
            rem = action[1] % 360
            for turn in range(0, rem, 90):
                current_dir = left_90[current_dir]
                current_wp = [current_wp[1] * -1, current_wp[0]]
        elif action[0] == 'R':
            rem = action[1] % 360
            for turn in range(0, rem, 90):
                current_dir = right_90[current_dir]
                current_wp = [current_wp[1], current_wp[0] * -1]
        elif action[0] == 'F':
            current_pos = [current_pos[0] + action[1] * current_wp[0], current_pos[1] + action[1] * current_wp[1]]
        elif action[0] == 'N':
            current_wp[1] += action[1]
        elif action[0] == 'S':
            current_wp[1] -= action[1]
        elif action[0] == 'E':
            current_wp[0] += action[1]
        elif action[0] == 'W':
            current_wp[0] -= action[1]
    return abs(current_pos[0]) + abs(current_pos[1])


with open("12_input.txt", "r") as f:
    actions = []
    for x in f:
        temp_ = x.rstrip()
        actions.append([temp_[0], int(temp_[1:])])

left_90 = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
right_90 = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}

print(do_actions(actions))