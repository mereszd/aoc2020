def move_ship(action, current_pos):
    if action[0] == 'N':
        current_pos[1] += action[1]
    elif action[0] == 'S':
        current_pos[1] -= action[1]
    elif action[0] == 'E':
        current_pos[0] += action[1]
    elif action[0] == 'W':
        current_pos[0] -= action[1]
    return current_pos


def do_actions(actions):
    current_dir = 'E'
    current_pos = [0, 0]
    for action in actions:
        if action[0] == 'L':
            rem = action[1] % 360
            for turn in range(0, rem, 90):
                current_dir = left_90[current_dir]
        elif action[0] == 'R':
            rem = action[1] % 360
            for turn in range(0, rem, 90):
                current_dir = right_90[current_dir]
        elif action[0] == 'F':
            current_pos = move_ship([current_dir, action[1]], current_pos)
        else:
            current_pos = move_ship(action, current_pos)
    return abs(current_pos[0]) + abs(current_pos[1])


with open("12_input.txt", "r") as f:
    actions = []
    for x in f:
        temp_ = x.rstrip()
        actions.append([temp_[0], int(temp_[1:])])

left_90 = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
right_90 = {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}

print(do_actions(actions))