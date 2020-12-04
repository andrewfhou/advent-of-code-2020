import time
import re

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 04 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split('\n\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

codes = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def part_one():
    valid = 0
    for ps in inputs:
        v = 1
        for c in codes:
            if not c in ps:
                v = 0
        valid += v
    return valid

def part_two():
    valid = 0
    for fields in [x.split() for x in inputs]:
        ps = set()
        for lb, val in [field.split(':') for field in fields]:
            if validate(lb, val): ps.add(lb)
        if ps & codes == codes:
            valid += 1
    return valid

def validate(lb, val):
    if lb == 'byr':
        return 1920 <= int(val) <= 2002
    elif lb == 'iyr':
        return 2010 <= int(val) <= 2020
    elif lb == 'eyr':
        return 2020 <= int(val) <= 2030
    elif lb == 'hgt':
        if val[-2:] == 'cm':
            return 150 <= int(val[:-2]) <= 193
        elif val[-2:] == 'in':
            return 59 <= int(val[:-2]) <= 76
    elif lb == 'hcl':
        return re.compile(r'^#[0-9a-f]{6}$').match(val)
    elif lb == 'ecl':
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif lb == 'pid':
        return re.compile(r'^\d{9}$').match(val)
    return False

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
