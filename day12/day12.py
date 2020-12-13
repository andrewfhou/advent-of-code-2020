import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 12 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split()
print('%.6fms\n' % (CURR_MS() - START_READ))

dirs = {0 : 'E', 90 : 'N', 180 : 'W', 270 : 'S'}

def part_one():
    x = y = curr_dir = 0

    for instr in inputs:
        op = instr[0]
        val = int(instr[1:])

        if op == 'L':
            curr_dir = (curr_dir + val) % 360
        elif op == 'R':
            curr_dir = (curr_dir - val) % 360
        elif op == 'F':
            x, y = travel(x, y, dirs[curr_dir], val)
        else:
            x, y = travel(x, y, op, val)
    return abs(x) + abs(y)

def travel(x, y, op, val):
    if op == 'N':
        y += val
    elif op == 'S':
        y -= val
    elif op == 'E':
        x += val
    elif op == 'W':
        x -= val
    return x, y

def part_two():
    x_wp = 10
    y_wp = 1
    x = y = 0

    for instr in inputs:
        op = instr[0]
        val = int(instr[1:])

        if op == 'L':
            x_wp, y_wp = rotate_wp(x_wp, y_wp, val % 360)
        elif op == 'R':
            x_wp, y_wp = rotate_wp(x_wp, y_wp, (-val) % 360)
        elif op == 'F':
            x += x_wp * val
            y += y_wp * val
        else:
            x_wp, y_wp = travel(x_wp, y_wp, op, val)
    return abs(x) + abs(y)

def rotate_wp(x, y, rot):
    if rot == 90:
        return -y, x
    elif rot == 180:
        return -x, -y
    elif rot == 270:
        return y, -x

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
