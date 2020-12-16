import time
import copy

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 16 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example1.txt") as file:
# with open("example2.txt") as file:
    inputs = file.read().split('\n\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    rules = {}
    valid_rng = set()
    for rule in inputs[0].split('\n'):
        range1 = [int(x) for x in rule.split(': ')[1].split(' ')[0].split('-')]
        range1 = set(range(range1[0], range1[1] + 1))
        range2 = [int(x) for x in rule.split(': ')[1].split(' ')[2].split('-')]
        range2 = set(range(range2[0], range2[1] + 1))
        rules[rule.split(':')[0]] = (range1 | range2)
        valid_rng |= rules[rule.split(':')[0]]

    err_rate = 0
    for ticket in inputs[2].split('\n')[1:-1]:
        valid_tix = True
        for val in ticket.split(','):
            if not int(val) in valid_rng:
                err_rate += int(val)
    return err_rate

def part_two():
    rules = {}
    valid_rng = set()
    for rule in inputs[0].split('\n'):
        range1 = [int(x) for x in rule.split(': ')[1].split(' ')[0].split('-')]
        range1 = set(range(range1[0], range1[1] + 1))
        range2 = [int(x) for x in rule.split(': ')[1].split(' ')[2].split('-')]
        range2 = set(range(range2[0], range2[1] + 1))
        rules[rule.split(':')[0]] = (range1 | range2)
        valid_rng |= rules[rule.split(':')[0]]

    tickets = []
    for ticket in inputs[2].split('\n')[1:-1]:
        valid_tix = True
        for val in ticket.split(','):
            if not int(val) in valid_rng:
                valid_tix = False
        if valid_tix:
            tickets.append([int(x) for x in ticket.split(',')])

    mine = [int(x) for x in inputs[1].split('\n')[1].split(',')]

    pos = {}
    for x in range(len(mine)):
        pos[x] = set(rules.keys())
    for ticket in tickets:
        for idx, val in enumerate(ticket):
            for rule in rules:
                if val not in rules[rule]:
                    pos[idx].remove(rule)
    options = {}
    for x in pos:
        options[len(pos[x])] = x
    for x in range(len(pos)):
        field = list(pos[options[x + 1]])[0]
        for rule in pos:
            if len(pos[rule]) > 1:
                pos[rule].remove(field)
    soln = {}
    for x in pos:
        field = pos[x].pop()
        if field.startswith('departure'):
            soln[field] = x
    ret = 1
    for x in soln.values():
        ret *= mine[x]
    return ret

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
