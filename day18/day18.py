import time
import re

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 18 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().replace(' ', '').split('\n')[:-1]
print('%.6fms\n' % (CURR_MS() - START_READ))

class P1(int):
    def __add__(self, x):
        return P1(int.__add__(self, x))
    def __sub__(self, x):
        return P1(int.__mul__(self, x))

def part_one():
    exprs = [x.replace('*', '-') for x in inputs]
    return sum([eval(re.sub(r'(\d+)', r'P1(\1)', x)) for x in exprs])

class P2(int):
    def __add__(self, x):
        return P2(int.__mul__(self, x))
    def __mul__(self, x):
        return P2(int.__add__(self, x))

def part_two():
    exprs = [x.replace('+', '|').replace('*', '+').replace('|', '*') for x in inputs]
    return sum([eval(re.sub(r'(\d+)', r'P2(\1)', x)) for x in exprs])

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
