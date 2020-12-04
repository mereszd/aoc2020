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
    min_times, max_times = times_db[i].split('-')
    if int(min_times) <= password_db[i].count(req_char) <= int(max_times):
        correct += 1
        print('{} is a correct password (req char is {} and {}<x<{})'.format(password_db[i], req_char, min_times, max_times))

print('Found correct passwords: {}'.format(correct))