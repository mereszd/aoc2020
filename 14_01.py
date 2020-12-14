with open("14_input.txt", "r") as f:
    instructions = []
    for x in f:
        instructions.append(x.rstrip())

current_mask = ''
mem = {}

for inst in instructions:
    if inst[0:2] == 'ma':
        t1, t2, current_mask = inst.split(' ')
    else:
        t1, t2, init_value = inst.split(' ')
        init_value = str(bin(int(init_value)))[2:]
        pos = t1[4:-1]
        diff = len(current_mask) - len(init_value)
        init_value = '0'*diff + init_value
        masked_number = ''
        for i in range(len(current_mask)):
            if current_mask[i] != 'X':
                masked_number += current_mask[i]
            else:
                masked_number += init_value[i]
        value = int('0b' + masked_number, 2)
        mem[pos] = value

sum = 0
for k in mem.keys():
    sum += mem[k]

print(sum)