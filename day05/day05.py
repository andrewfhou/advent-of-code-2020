import time
import math

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 05 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    hi = 0
    for seat in inputs:
        seat = seat.replace('F', '0').replace('B', '1').replace('L','0').replace('R', '1')
        hi = max(int(seat, 2), hi)
    return hi

def part_two():
    cabin = set()
    for seat in inputs:
        seat = seat.replace('F', '0').replace('B', '1').replace('L','0').replace('R', '1')
        cabin.add(int(seat, 2))
    for x in range(127 * 8):
        if x not in cabin and x+1 in cabin and x-1 in cabin:
            return x

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
