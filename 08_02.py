import copy

def run_instructions(instructions):
    already_ran = []
    i = 0
    accum = 0
    while True:
        if i == len(instructions):
            run = False
            print('Found the correct sequence. Acc is {}'.format(accum))
            break
        if i not in already_ran:
            if instructions[i][0] == 'acc':
                accum += instructions[i][1]
                already_ran.append(i)
                i += 1
            elif instructions[i][0] == 'jmp':
                already_ran.append(i)
                i += instructions[i][1]
            elif instructions[i][0] == 'nop':
                already_ran.append(i)
                i += 1
        else:
            break
    return accum


with open("08_input.txt", "r") as f:
    instructions = []
    for x in f:
        inst, value = x.rstrip().split(' ')
        if value[0] == '+':
            value = int(value[1:])
        else:
            value = int(value)
        instructions.append([inst, value])

for j in range(len(instructions)):
    if instructions[j][0] == 'nop':
        _temp = copy.deepcopy(instructions)
        _temp[j][0] = 'jmp'
        print(run_instructions(_temp))
    elif instructions[j][0] == 'jmp':
        _temp = copy.deepcopy(instructions)
        _temp[j][0] = 'nop'
        print(run_instructions(_temp))