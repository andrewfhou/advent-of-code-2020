import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 20 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
# with open("input.txt") as file:
with open("example.txt") as file:
    inputs = file.read().strip().split('\n\n')
    tiles = {}
    for tile in inputs:
        tiles[int(tile.split('\n')[0].split(' ')[1][:-1])] = tile.split('\n')[1:]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    print(tiles)
    return 0

def part_two():
    return 0

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
