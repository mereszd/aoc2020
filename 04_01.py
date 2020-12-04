passports = []
passports_dict = []
_temp = ''


def validate_passport(passport):
    req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    # Checking for required fields
    for req_field in req_fields:
        if req_field not in passport.keys():
            print('{} is invalid because {} is missing'.format(passport, req_field))
            return False
    # Validating Birth year
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        print('{} is invalid because byr is incorrect'.format(passport))
        return False
    # Validating Issue year
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        print('{} is invalid because iyr is incorrect'.format(passport))
        return False
    # Validating Expiration year
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        print('{} is invalid because eyr is incorrect'.format(passport))
        return False
    # Validating Height
    if passport['hgt'][-2:] == 'cm':
        if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
            print('{} is invalid because hgt is incorrect in cm'.format(passport))
            return False
    elif passport['hgt'][-2:] == 'in':
        if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
            print('{} is invalid because hgt is incorrect in in'.format(passport))
            return False
    else:
        print('{} is invalid because hgt doesnt end with cm or in'.format(passport))
        return False
    # Validating Hair Color
    if passport['hcl'][0] == '#':
        if len(passport['hcl']) != 7:
            print('{} is invalid because hcl isnt 7 characters'.format(passport))
            return False
        for i in range(1, 7):
            if passport['hcl'][i] in '0123456789' or passport['hcl'][i] in 'abcdef':
                pass
            else:
                print('{} is invalid because digit {} in hcl isnt correct'.format(passport, i))
                return False
    else:
        print('{} is invalid because hcl doesnt start with #'.format(passport))
        return False
    # Validating Eye Color
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if passport['ecl'] not in valid_eye_colors:
        print('{} is invalid because ecl is invalid'.format(passport))
        return False
    # Validating Passport ID
    if len(passport['pid']) != 9:
        print('{} is invalid because pid isnt the correct length'.format(passport))
        return False
    else:
        for i in range(9):
            if passport['pid'][i] in '0123456789':
                pass
            else:
                print('{} is invalid because digit {} in pid is incorrect'.format(passport, i))
                return False
    return True


with open("04_input.txt", "r") as f:
    for x in f:
        if x.rstrip() == '':
            passports.append(_temp)
            _temp = ''
        else:
            if _temp != '':
                _temp = _temp + ' ' + x.rstrip()
            else:
                _temp = x.rstrip()
    passports.append(_temp)

for passport in passports:
    temp_dict = {}
    passport_split = passport.split(' ')
    for x in passport_split:
        i, j = x.split(':')
        temp_dict[i] = j
    passports_dict.append(temp_dict)

valid_passports_count = 0
valid_passports = []
invalid_passports = []

for passport in passports_dict:
    if validate_passport(passport):
        valid_passports_count += 1
        valid_passports.append(passport)
    else:
        invalid_passports.append(passport)

print(valid_passports_count)