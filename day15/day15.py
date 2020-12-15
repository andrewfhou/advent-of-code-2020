import time
from collections import defaultdict

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 15 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split(',')
    inputs = [int(x) for x in inputs]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    spoken = defaultdict(list)
    for x, num in enumerate(inputs):
        spoken[num].append(x + 1)
    prev = inputs[-1]
    for turn in range(len(inputs) + 1, 2020 + 1):
        if len(spoken[prev]) > 1:
            delt = spoken[prev][-1] - spoken[prev][-2]
            prev = delt
            spoken[delt].append(turn)
        else:
            spoken[0].append(turn)
            prev = 0
    return prev

def part_two():
    spoken = defaultdict(list)
    for x, num in enumerate(inputs):
        spoken[num].append(x + 1)
    prev = inputs[-1]
    for turn in range(len(inputs) + 1, 30000000 + 1):
        if len(spoken[prev]) > 1:
            delt = spoken[prev][-1] - spoken[prev][-2]
            prev = delt
            spoken[delt].append(turn)
        else:
            spoken[0].append(turn)
            prev = 0
    return prev

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
