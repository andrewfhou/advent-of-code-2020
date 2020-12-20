import time
import math
import itertools

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 20 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split('\n\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    tiles = {}
    for tile in inputs:
        lines = tile.strip().split('\n')
        tiles[lines[0].split(' ')[1][:-1]] = transforms(lines[1:])

    side_len = int(math.sqrt(len(tiles)))
    img = [[0] * side_len for _ in range(side_len)]
    coords = list(reversed(list((r, c) for c in range(side_len) for r in range(side_len))))
    solve_img(tiles, coords, img)
    return int(img[0][0][0]) * int(img[-1][0][0]) * int(img[0][-1][0]) * int(img[-1][-1][0])

def part_two():
    tiles = {}
    for tile in inputs:
        lines = tile.strip().split('\n')
        tiles[lines[0].split(' ')[1][:-1]] = transforms(lines[1:])

    side_len = int(math.sqrt(len(tiles)))
    img = [[0] * side_len for _ in range(side_len)]
    coords = list(reversed(list((r, c) for c in range(side_len) for r in range(side_len))))
    solve_img(tiles, coords, img)
    board = [[trim(tile[1]) for tile in row] for row in img]
    board = [''.join(get(board, r, c) for c in range(side_len * 8)) for r in range(side_len * 8)]

    monster = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']

    for transform in transforms(monster):
        monsters = 0
        for rs in range(len(board) - len(monster) + 1):
            for cs in range(len(board[0]) - len(monster[0]) + 1):
                matching = 1
                for r in range(len(monster)):
                    for c in range(len(monster[0])):
                        if monster[r][c] == '#' and board[r + rs][c + cs] !='#':
                            matching = 0
                monsters += matching
        if monsters:
            return ''.join(board).count('#') - ''.join(monster).count('#') * monsters

def get(board, r, c):
    return board[r // 8][c // 8][r % 8][c % 8]

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

def solve_img(tiles, coords, img):
    if len(coords) == 0:
        return True
    (r, c) = coords.pop()
    for tile_num in list(tiles.keys()):
        tile_tfs = tiles[tile_num]
        del tiles[tile_num]
        for tile in tile_tfs:
            if r > 0 and img[r - 1][c][1][-1] != tile[0]:
                continue
            if c > 0 and list(row[-1] for row in img[r][c - 1][1]) != list(row[0] for row in tile):
                continue
            img[r][c] = (tile_num, tile)
            if solve_img(tiles, coords, img):
                return True
        tiles[tile_num] = tile_tfs
    coords.append((r, c))

def trim(tile):
    return [row[1:-1] for row in tile[1:-1]]

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
