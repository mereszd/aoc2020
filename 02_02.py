input_db = []
times_db = []
char_db = []
password_db = []
correct = 0

with open("02_input.txt", "r") as f:
    for x in f:
        input_db.append(x.rstrip())

for input in input_db:
    x, y, z = input.split(' ')
    times_db.append(x)
    char_db.append(y)
    password_db.append(z)

for i in range(len(input_db)):
    req_char = char_db[i][0]
    first_pos, second_pos = times_db[i].split('-')
    first_char = password_db[i][int(first_pos)-1]
    second_char = password_db[i][int(second_pos)-1]
    if first_char == req_char and second_char == req_char:
        pass
    elif first_char == req_char:
        print("{} is a correct password because {} is at {} position".format(password_db[i], first_char, first_pos))
        correct += 1
    elif second_char == req_char:
        print("{} is a correct password because {} is at {} position".format(password_db[i], second_char, second_pos))
        correct += 1


print('Found correct passwords: {}'.format(correct))