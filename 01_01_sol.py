input_array = []
des_sum = 2020
found = False
result = 0

with open("01_01_input.txt", "r") as f:
    for x in f:
        input_array.append(int(x.strip()))

input_array.sort()

back_index = len(input_array) -1
front_index = 0

while found is False:
    current_sum = input_array[front_index] + input_array[back_index]
    print("{}: {}  {}: {}  sum: {}".format(front_index, input_array[front_index], back_index, input_array[back_index], current_sum))
    if current_sum > des_sum:
        print("Current sum is higher")
        back_index = back_index - 1
    elif current_sum < des_sum:
        print("Current sum is lower")
        front_index = front_index + 1
        back_index = len(input_array) - 1
    else:
        print("Found it")
        result = input_array[front_index] * input_array[back_index]
        print(result)
        found = True