instructions = []

def run_instructions(instructions):
    run = True
    already_ran = []
    i = 0
    accum = 0
    while run:
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
            run = False
    return accum


with open("08_input.txt", "r") as f:
    for x in f:
        inst, value = x.rstrip().split(' ')
        if value[0] == '+':
            value = int(value[1:])
        else:
            value = int(value)
        instructions.append([inst, value])

print(run_instructions(instructions))