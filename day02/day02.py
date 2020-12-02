import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 02 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split('\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    valid = 0
    for line in inputs:
        rng, char, pss = line.split(' ')
        char = char[0]
        lo, hi = [int(x) for x in rng.split('-')]
        count = pss.count(char)
        if count in range(lo, hi + 1):
            valid += 1
    return valid

def part_two():
    valid = 0
    for line in inputs:
        rng, char, pss = line.split(' ')
        char = char[0]
        lo, hi = [int(x) for x in rng.split('-')]
        if (pss[lo - 1] == char) ^ (pss[hi - 1] == char):
            valid += 1
    return valid

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
