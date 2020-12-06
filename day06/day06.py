import time
import functools

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 06 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    return sum(len(set(group.replace('\n',''))) for group in inputs.split('\n\n'))

def part_two():
    return sum(len(functools.reduce(
                     lambda a, b: a.intersection(b),
                     map(set, group.split('\n')),
                     set(group.replace('\n', ''))))
               for group in inputs.split('\n\n'))

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
