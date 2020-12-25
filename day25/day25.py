import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 25 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    return find_key(int(inputs[0]), find_loop(int(inputs[1])))

def find_loop(pub_key):
    loop = 0
    res = 1
    while True:
        loop += 1
        res *= 7
        res %= 20201227
        if res == pub_key:
            return loop

def find_key(subj, loop):
    find_loop_key = 1
    for _ in range(loop):
        find_loop_key = find_loop_key * subj
        find_loop_key = find_loop_key % 20201227
    return find_loop_key

def part_two():
    return 'done!'

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
