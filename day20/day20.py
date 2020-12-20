import time
import math
import itertools

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 20 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
# with open("input.txt") as file:
with open("example.txt") as file:
    inputs = file.read().strip().split('\n\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    edges = []
    tiles = []
    for x in range(len(inputs)):
        e = find_edges(inputs[x].split('\n'))
        edges.append(e)
        tiles.append(e)

    soln = 1
    for tile in tiles:
        uniques = 0
        for edge in tile[1:]:
            if list(itertools.chain(*tiles)).count(edge) == 1:
                uniques += 1
        if uniques == 4: # 4 uniques means 2 unique edges (fwd/rev)
            soln *= int(tile[0].split(' ')[1][:-1])
    return soln

def find_edges(t):
    return [
            t[0],                                  # tile #
            t[1],                                  # N; W -> E
            t[1][::-1],                            # N; E -> W
            t[-1],                                 # S; W -> E
            t[-1][::-1],                           # S; E -> W
            ''.join([x[0] for x in t[1:]]),        # W; N -> S
            ''.join([x[0] for x in t[1:]])[::-1],  # W; S -> N
            ''.join([x[-1] for x in t[1:]]),       # E; N -> S
            ''.join([x[-1] for x  in t[1:]])[::-1] # E; S -> N
    ]

def part_two():
    tiles = {}
    for tile in inputs:
        lines = tile.strip().split('\n')
        tiles[lines[0]] = transforms(lines[1:])

    side = int(math.sqrt(len(tiles)))
    img = [[0] * side for _ in range(side)]
    coords = list(reversed(list((r, c) for c in range(side) for r in range(side))))
    print(coords)
    return 0

def transpose(tile):
    return list(''.join(row) for row in zip(*tile))

def reverse(tile):
    return [''.join(reversed(row)) for row in tile]

def make_rotations(tile):
    ret = [tile]
    for _ in range(3):
        ret.append(reverse(transpose(ret[-1])))
    return ret

def transforms(tile):
    return make_rotations(tile) + make_rotations(transpose(tile))

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
