import time
import copy

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 23 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = [int(x) for x in file.read().strip()]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    cups = copy.deepcopy(inputs)
    hi = max(cups)
    curr = cups[0]
    for mov in range(100):
        crab = []
        for i in range(3):
            crab.append(cups.pop((cups.index(curr) + 1) % len(cups)))
        dest = curr - 1
        while True:
            if dest == 0:
                dest = hi
            if dest not in crab:
                break
            dest -= 1
        for i in range(3):
            idx = (cups.index(dest) + i + 1) % len(inputs)
            if idx >= len(cups):
                cups.append(crab[i])
            else:
                cups.insert(idx, crab[i])
        curr = cups[(cups.index(curr) + 1) % len(inputs)]
    ret = ''
    for i in range(len(cups) - 1):
        ret += str(cups[(cups.index(1) + i + 1) % len(cups)])
    return ret

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def part_two():
    cups = {}
    prev = None
    for i in inputs:
        cup = Node(i)
        cups[i] = cup
        if prev is not None:
            prev.right = cup
            cup.left = prev
        prev = cup

    for i in range(len(inputs) + 1, 1000001):
        cup = Node(i)
        cups[i] = cup
        if prev is not None:
            prev.right = cup
            cup.left = prev
        prev = cup

    temp = cups[inputs[0]]
    prev.right = temp
    temp.left = prev

    curr = cups[inputs[0]]
    for i in range(10000000):
        val = curr.val
        cup1 = curr.right
        cup2 = cup1.right
        cup3 = cup2.right

        curr.right = cup3.right
        curr.right.left = curr

        dest = val - 1 if val != 1 else 1000000
        while dest in (cup1.val, cup2.val, cup3.val):
            dest = dest - 1 if val != 1 else 1000000
        dest_node = cups[dest]
        cup3.right = dest_node.right
        cup3.right.left = cup3
        dest_node.right = cup1
        cup1.left = dest_node

        curr = curr.right

    while curr.val != 1:
        curr = curr.right
    return curr.right.val * curr.right.right.val

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
