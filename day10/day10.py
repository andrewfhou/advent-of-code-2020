import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 10 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split()
    inputs = [int(x) for x in inputs]
    inputs.append(0)
    inputs.append(max(inputs) + 3)
    inputs.sort()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    delt1 = 0
    delt3 = 0
    for i in range(len(inputs) - 1):
        delta = inputs[i + 1] - inputs[i]
        if delta == 1: delt1 += 1
        else: delt3 += 1
    return delt1 * delt3

def part_two():
    count = [0] * len(inputs)
    count[0] = 1
    for i in range(len(inputs)):
        for j in range(0, i):
            if inputs[i] - inputs[j] <= 3:
                count[i] += count[j]
    return count[-1]

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
