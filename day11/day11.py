import time
import copy

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 11 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split()
    inputs = [list(x) for x in inputs]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    grid = copy.deepcopy(inputs)
    changed = True
    while changed:
        grid, changed = step_simple(grid)
    return sum(row.count('#') for row in grid)

def step_simple(grid):
    r, c = len(grid), len(grid[0])
    new = copy.deepcopy(grid)
    changed = False
    for row in range(r):
        for col in range(c):
            adj = 0
            adj += row         and col         and grid[row - 1][col - 1] == '#'
            adj += row                         and grid[row - 1][col    ] == '#'
            adj += row         and col + 1 < c and grid[row - 1][col + 1] == '#'

            adj += col                         and grid[row    ][col - 1] == '#'
            adj += col + 1 < c                 and grid[row    ][col + 1] == '#'

            adj += row + 1 < r and col         and grid[row + 1][col - 1] == '#'
            adj += row + 1 < r                 and grid[row + 1][col    ] == '#'
            adj += row + 1 < r and col + 1 < c and grid[row + 1][col + 1] == '#'

            if grid[row][col] == 'L' and adj == 0:
                changed = True
                new[row][col] = '#'
            elif grid[row][col] == '#' and adj >= 4:
                changed = True
                new[row][col] = 'L'
    return new, changed

def part_two():
    grid = copy.deepcopy(inputs)
    changed = True
    while changed:
        grid, changed = step_complex(grid)
    return sum(row.count('#') for row in grid)

def los(grid, row, col, dir_r, dir_c):
    if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] == 'L':
        return False
    if grid[row][col] == '#':
        return True
    return los(grid, row + dir_r, col + dir_c, dir_r, dir_c)

def step_complex(grid):
    r, c = len(grid), len(grid[0])
    new = copy.deepcopy(grid)
    changed = False
    for row in range(r):
        for col in range(c):
            adj = 0
            adj += los(grid, row - 1, col - 1, -1, -1)
            adj += los(grid, row - 1, col,     -1,  0)
            adj += los(grid, row - 1, col + 1, -1 , 1)

            adj += los(grid, row,     col - 1,  0, -1)
            adj += los(grid, row,     col + 1,  0,  1)

            adj += los(grid, row + 1, col - 1,  1, -1)
            adj += los(grid, row + 1, col,      1,  0)
            adj += los(grid, row + 1, col + 1,  1,  1)

            if grid[row][col] == 'L' and adj == 0:
                changed = True
                new[row][col] = '#'
            elif grid[row][col] == '#' and adj >= 5:
                changed = True
                new[row][col] = 'L'
    return new, changed

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
