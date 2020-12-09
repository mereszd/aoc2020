def find_error(numbers):
    i = 25
    while i < len(numbers):
        valid = False
        to_find = numbers[i]
        start_index = i-25
        numb_slice = numbers[start_index:i]
        for number in numb_slice:
            if to_find - number in numb_slice:
                valid = True
                break
        if valid is False:
            return numbers[i]
        i += 1
    return "Couldn't find it"


with open("09_input.txt", "r") as f:
    numbers = []
    for x in f:
        numbers.append(int(x.rstrip()))

print(find_error(numbers))