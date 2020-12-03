import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 03 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one(right, down):
    row = 0
    shift = 0
    trees = 0

    while True:
        if (inputs[row])[shift] == '#':
            trees += 1
        shift = (shift + right) % len(inputs[0])
        row += down
        if row >= len(inputs):
            return trees

def part_two():
    return part_one(1, 1) * part_one(3, 1) * part_one(5, 1) * part_one(7, 1) * part_one(1, 2)

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one(3, 1)))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
