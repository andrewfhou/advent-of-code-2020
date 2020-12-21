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

def part_one():
    foods = parse()
    all_ing = set()
    all_all = set()
    for ings, allgs in foods:
        all_ing |= ings
        all_all |= allgs

    possible = set()
    for allergen in all_all:
        ps = set(all_ing)
        for ings, allgs in foods:
            if allergen in allgs:
                ps &= ings
        possible |= ps

    safe = all_ing - possible
    soln = 0
    for ings, allgs in foods:
        soln += len(ings & safe)
    return soln

def parse():
    foods = []
    for line in inputs:
        ingredients = set(line.split(' (contains ')[0].split(' '))
        allergens = set(line.split(' (contains ')[1].split(' '))
        foods.append((ingredients, allergens))
    return foods

def part_two():
    foods = parse()
    all_ing = set()
    all_all = set()
    for ings, allgs in foods:
        all_ing |= ings
        all_all |= allgs

    possible = set()
    for allergen in all_all:
        ps = set(all_ing)
        for ings, allgs in foods:
            if allergen in allgs:
                ps &= ings
        possible |= ps

    trans = {}
    for allergen in all_all:
        trans[allergen] = set(possible)
    for ings, alls in foods:
        for allergen in alls:
            trans[allergen] &= ings

    while not all(len(x) <= 1 for x in trans.values()):
        found = set()
        for x in trans.values():
            if len(x) == 1:
                found |= x
        for allgn, x in trans.items():
            if len(x) > 1:
                trans[allgn] -= found
    words = sorted(trans.items())
    return ','.join(list(x)[0] for _, x in words)

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
