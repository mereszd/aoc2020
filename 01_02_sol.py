def find_sum(des_sum):
    found = False
    back_index = len(input_array) - 1
    front_index = 0
    result = 0

    while found is False:
        if front_index == back_index:
            print("Couldn't find it")
            break
        current_sum = input_array[front_index] + input_array[back_index]
        print(
            "{}: {}  {}: {}  sum: {}".format(front_index, input_array[front_index], back_index, input_array[back_index],
                                             current_sum))
        if current_sum > des_sum:
            print("Current sum is higher")
            back_index = back_index - 1
        elif current_sum < des_sum:
            print("Current sum is lower")
            front_index = front_index + 1
            back_index = len(input_array) - 1
        else:
            print("Found it")
            found = True

    if found is True:
        return input_array[front_index], input_array[back_index]
    else:
        return False, False


input_array = []

with open("01_01_input.txt", "r") as f:
    for x in f:
        input_array.append(int(x.strip()))

input_array.sort()

for x in input_array:
    second, third = find_sum(2020-x)
    if second is not False:
        print("Answer is {}. The values are {}, {}, {}.".format(x*second*third, x, second, third))
        break