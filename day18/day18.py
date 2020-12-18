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

def part_one():
    total = 0
    for expr in inputs:
        total += calc(expr, 0, len(expr))
    return total

def calc(expr, start, end):
    curr = start
    soln = 0
    add = True

    while curr < end:
        if expr[curr] == '+':
            add = True
        elif expr[curr] == '*':
            add = False
        elif expr[curr] == '(':
            parens = 1
            paren_close = curr + 1
            while parens > 0:
                if expr[paren_close] == ')':
                    parens -= 1
                elif expr[paren_close] == '(':
                    parens += 1
                paren_close += 1
            paren_close -= 1

            if add: soln += calc(expr, curr + 1, paren_close)
            else: soln *= calc(expr, curr + 1, paren_close)
            curr = paren_close
        else:
            if add: soln += int(expr[curr])
            else: soln *= int(expr[curr])
        curr += 1
    return soln

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
