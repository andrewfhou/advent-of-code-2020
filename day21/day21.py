import time
from collections import defaultdict
import copy
import re

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 21 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().replace(')', '').replace(',', '').split('\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

foods = []
for line in inputs:
    ings = set(line.split(' (contains ')[0].split(' '))
    allgs = set(line.split(' (contains ')[1].split(' '))
    foods.append((ings, allgs))

all_ings = set()
all_allgs = set()
for ings, allgs in foods:
    all_ings |= ings
    all_allgs |= allgs

possible = set()
for allg in all_allgs:
    ps = set(all_ings)
    for ings, allgs in foods:
        if allg in allgs:
            ps &= ings
    possible |= ps

def part_one():
    return sum(len(ings & (all_ings - possible)) for ings, _ in foods)

def part_two():
    allgs_to_ings = {}
    for allg in all_allgs:
        allgs_to_ings[allg] = set(possible)
    for ings, allgs in foods:
        for allg in allgs:
            allgs_to_ings[allg] &= ings

    while not all(len(x) <= 1 for x in allgs_to_ings.values()):
        found = set()
        for x in allgs_to_ings.values():
            if len(x) == 1:
                found |= x
        for allg, ings in allgs_to_ings.items():
            if len(ings) > 1:
                allgs_to_ings[allg] -= found
    return ','.join(list(x)[0] for _, x in sorted(allgs_to_ings.items()))

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
