import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 01 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split()
    inputs = [int(x) for x in inputs]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    s = set()
    for x in inputs:
        test = 2020 - x
        if test in s:
            return test * x
        else:
            s.add(x)

def part_two():
    for i in range(len(inputs)):
        s = set()
        sm = 2020 - inputs[i]
        for j in range(i + 1, len(inputs)):
            if (sm - inputs[j]) in s:
                return inputs[j] * inputs[i] * (sm - inputs[j])
            s.add(inputs[j])

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
