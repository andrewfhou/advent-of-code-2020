import time
import itertools

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 14 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split('\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    mask = ''
    mem = {}

    for instr in inputs:
        if instr.split(' = ')[0] == 'mask':
            mask = instr.split(' = ')[1]
        else:
            addr = int(instr.split(' = ')[0][4:-1])
            val = str(bin(int(instr.split(' = ')[1])).replace('0b','')).zfill(len(mask))
            mem[addr] = int(apply_mask(mask, val), 2)
    return sum(mem.values())

def apply_mask(mask, val):
    out = ''
    for i in range(len(mask)):
        if mask[i] != 'X':
            out += mask[i]
        else:
            out += val[i]
    return out

def part_two():
    mask = ''
    mem = {}

    for instr in inputs:
        if instr.split(' = ')[0] == 'mask':
            mask = instr.split(' = ')[1]
        else:
            addr = str(bin(int(instr.split(' = ')[0][4:-1])).replace('0b','')).zfill(len(mask))
            val = int(instr.split(' = ')[1])

            addr = apply_mask_v2(mask, addr)
            write_val(mem, addr, val)
    return sum(mem.values())

def write_val(mem, addr, val):
    if 'X' in addr:
        write_val(mem, addr.replace('X', '0', 1), val)
        write_val(mem, addr.replace('X', '1', 1), val)
    else:
        mem[int(addr, 2)] = val

def apply_mask_v2(mask, val):
    out = ''
    for i in range(len(val)):
        if mask[i] == '0':
            out += val[i]
        elif mask[i] == '1':
            out += '1'
        else:
            out += 'X'
    return out

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
