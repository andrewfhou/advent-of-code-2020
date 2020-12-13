import time
import copy
from functools import reduce

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 13 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split()
    inputs[1] = [int(x) if x!= 'x' else None for x in inputs[1].split(',')]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    t = int(inputs[0])
    busses = [x for x in inputs[1] if x != None]
    best = busses[0]
    best_d = (int(t / best) + 1) * best
    for bus in busses:
        depart = (int(t / bus) + 1) * bus
        if depart < best_d:
            best = bus
            best_d = depart
    return (best_d - t) * best

def part_two():
    busses = inputs[1]
    n = list()
    a = list()
    for x, time in enumerate(busses):
        if time:
            n.append(int(time))
            a.append(int(time) - int(x))
    return crt(n, a)

def crt(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
