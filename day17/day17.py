import time
from collections import defaultdict
import copy

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 17 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().replace('.', '0').replace('#', '1').split()
    inputs = [list(x) for x in inputs]
    inputs = [[int(x) for x in row] for row in inputs]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    active = []
    for row in range(len(inputs)):
        for col in range(len(inputs[row])):
            if inputs[row][col]:
                active.append((row, col, 0))
    for _ in range(6):
        active = cycle(active)
    return len(active)

def find_neighbours(pt):
    x, y, z = pt
    for x_shift in (-1, 0, 1):
        for y_shift in (-1, 0, 1):
            for z_shift in (-1, 0, 1):
                if x_shift == y_shift == z_shift == 0:
                    continue
                yield (x + x_shift, y + y_shift, z + z_shift)

def cycle(prev):
    active = defaultdict(int)
    for pt in prev:
        for neighbour in find_neighbours(pt):
            active[neighbour] += 1
    new_active = []
    for pt in prev:
        count = active.pop(pt, 0)
        if count == 2 or count == 3:
            new_active.append(pt)
    for pt, count in active.items():
        if count == 3:
            new_active.append(pt)
    return new_active

def part_two():
    active = []
    for row in range(len(inputs)):
        for col in range(len(inputs[row])):
            if inputs[row][col]:
                active.append((row, col, 0, 0))
    for _ in range(6):
        active = hypercycle(active)
    return len(active)

def find_hyper_neighbours(pt):
    x, y, z, w = pt
    for x_shift in (-1, 0, 1):
        for y_shift in (-1, 0, 1):
            for z_shift in (-1, 0, 1):
                for w_shift in (-1, 0, 1):
                    if x_shift == y_shift == z_shift == w_shift == 0:
                        continue
                    yield (x + x_shift, y + y_shift, z + z_shift, w + w_shift)

def hypercycle(prev):
    active = defaultdict(int)
    for pt in prev:
        for neighbour in find_hyper_neighbours(pt):
            active[neighbour] += 1
    new_active = []
    for pt in prev:
        count = active.pop(pt, 0)
        if count == 2 or count == 3:
            new_active.append(pt)
    for pt, count in active.items():
        if count == 3:
            new_active.append(pt)
    return new_active

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
