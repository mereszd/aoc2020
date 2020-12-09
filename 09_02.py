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

def find_consec(number, numbers):
    for i in range(len(numbers)):
        numb_list = [numbers[i]]
        sum = numbers[i]
        for j in range(i+1, len(numbers)):
            sum += numbers[j]
            numb_list.append(numbers[j])
            if sum > number:
                break
            elif sum == number:
                return numb_list



with open("09_input.txt", "r") as f:
    numbers = []
    for x in f:
        numbers.append(int(x.rstrip()))

numb_range = find_consec(find_error(numbers), numbers)
print(min(numb_range) + max(numb_range))