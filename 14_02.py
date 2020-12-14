def gen_floating(bin):
    new_bin = ''
    float_values = []
    if 'X' not in bin:
        float_values.append(bin)
    else:
        for i in range(len(bin)):
            if bin[i] != 'X':
                new_bin += bin[i]
            else:
                f1 = new_bin + '0' + bin[i+1:]
                f2 = new_bin + '1' + bin[i+1:]
                break
        float_values += gen_floating(f1) + gen_floating(f2)
    return float_values


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
        init_value = int(init_value)
        pos = t1[4:-1]
        pos = str(bin(int(pos)))[2:]
        diff = len(current_mask) - len(pos)
        pos = '0'*diff + pos
        masked_pos = ''
        for i in range(len(current_mask)):
            if current_mask[i] == '0':
                masked_pos += pos[i]
            else:
                masked_pos += current_mask[i]
        floating_values = gen_floating(masked_pos)
        for fl in floating_values:
            fl_address = int('0b' + fl, 2)
            mem[fl_address] = init_value

sum = 0
for k in mem.keys():
    sum += mem[k]

print(sum)

# for fl in gen_floating('00000000000000000000000000000001X0XX'):
#     print('{} (decimal {})'.format(fl, int('0b' + fl, 2)))