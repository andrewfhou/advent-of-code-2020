import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 06 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split('\n\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    yes = 0
    for group in inputs:
        group = group.replace('\n', '')
        yes += len(''.join(set(group)))
    return yes

def part_two():
    yes = 0
    for group in inputs:
        group = group.replace('\n', ' ')
        yes += len(set.intersection(*map(set, group.split())))
    return yes

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
