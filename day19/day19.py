import time
import re

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 19 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split('\n\n')
    inputs = [x.split('\n') for x in inputs]

    rulelist = [x.split(' ') for x in inputs[0]]
    rulelist = [[int(x) if x.isdigit() else x for x in rule] for rule in rulelist]
    rules = {}
    for rule in rulelist:
        rules[int(rule[0][:-1])] = rule[1:]
    msgs = inputs[1]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    regex_str = '^' + eval_rule(0) + '$'
    regex = re.compile(regex_str)
    matches = 0
    for msg in msgs:
        if regex.match(msg):
            matches += 1
    return matches

def eval_rule(idx):
    if '\"a\"' in rules[idx]:
        return 'a'
    if '\"b\"' in rules[idx]:
        return 'b'
    else:
        if '|' in rules[idx]:
            rulestr = '('
            for x in rules[idx]:
                if '|' == x:
                    rulestr += '|'
                else:
                    rulestr += eval_rule(x)
            return rulestr + ')'
        else:
            rulestr = ''
            for num in rules[idx]:
                rulestr += eval_rule(num)
            return rulestr

def part_two():
    return 0

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
