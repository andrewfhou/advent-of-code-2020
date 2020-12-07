import time
from collections import defaultdict

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 07 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().replace(' no ', ' 0 ').split('\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    graph = defaultdict(list)
    for line in inputs:
        parent, child = line.split(' contain ')
        parent = ' '.join(parent.split()[0:2])
        for bag in child.split(', '):
            graph[' '.join(bag.split()[1:3])].append(parent)
    chain = set()
    return len(count_parents(graph, chain, 'shiny gold'))

def count_parents(graph, chain, color):
    if len(graph[color]) == 0: return chain
    chain.update(graph[color])
    for c in graph[color]:
        res = count_parents(graph, chain, c)
        if res != None: chain.update(res)
    return chain

def part_two():
    graph = defaultdict(list)
    for line in inputs:
        parent, child = line.split(' contain ')
        parent = ' '.join(parent.split()[0:2])
        for bag in child.split(', '):
            graph[parent].append([bag.split()[0], ' '.join(bag.split()[1:3])])
    return count_children(graph, 'shiny gold') - 1

def count_children(graph, color):
    if len(graph[color]) == 0: return 0
    return 1 + sum( int(x[0]) * count_children(graph, x[1]) for x in graph[color])

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
