import time
import copy

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 0 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split('\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    return run(inputs)[1]

def part_two():
    for lnum in range(len(inputs)):
        instr = inputs[lnum].split(' ')[0]
        if instr == 'nop':
            mod = copy.deepcopy(inputs)
            mod[lnum] = mod[lnum].replace('nop', 'jmp')
            ret = run(mod)
            if ret[0] != -1: return ret[1]
        elif instr == 'jmp':
            mod = copy.deepcopy(inputs)
            mod[lnum] = mod[lnum].replace('jmp', 'nop')
            ret = run(mod)
            if ret[0] != -1: return ret[1]

def run(code):
    acc = 0
    lnum = 0
    visited = set()
    while True:
        if lnum >= len(code): return [1, acc]
        line = code[lnum]
        if lnum in visited: return [-1, acc]
        visited.add(lnum)
        instr, arg = line.split(' ')
        if instr == 'acc':
            acc += int(arg)
            lnum += 1
        elif instr == 'jmp':
            lnum += int(arg)
        elif instr == 'nop':
            lnum += 1

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
