import time
import re
from collections import defaultdict

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 24 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split('\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

dirmap = {
        'e': (1, 0),
        'se': (0, -1),
        'sw': (-1, -1),
        'w': (-1, 0),
        'nw': (0, 1),
        'ne': (1,1),
        }

def part_one():
    floor = defaultdict(int)
    for line in inputs:
        x, y = 0, 0
        dirs = re.findall('e|se|sw|w|nw|ne', line)
        for d in dirs:
            x += dirmap[d][0]
            y += dirmap[d][1]
        floor[(x, y)] = not floor[(x, y)]
    return sum(floor.values())

def part_two():
    floor = defaultdict(int)
    for line in inputs:
        x, y = 0, 0
        dirs = re.findall('e|se|sw|w|nw|ne', line)
        for d in dirs:
            x += dirmap[d][0]
            y += dirmap[d][1]
        floor[(x, y)] = not floor[(x, y)]

    for x in range(100):
        floor = run(floor)
    return sum(floor.values())

def run(floor):
    adj = defaultdict(int)
    for k, v in floor.items():
        if v == 0:
            continue
        for a in [(1, 0), (0, -1), (-1, -1), (-1, 0), (0, 1), (1, 1)]:
            pt = (k[0] + a[0], k[1] + a[1])
            adj[pt] += 1
    new_floor = defaultdict(int)
    for k, v in floor.items():
        if v == 1:
            if adj[k] not in (1, 2):
                pass
            else:
                new_floor[k] = 1
    for k, v in adj.items():
        if v == 2 and floor[k] == 0:
            new_floor[k] = 1
    return new_floor

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
