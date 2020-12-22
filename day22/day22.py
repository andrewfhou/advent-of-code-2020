import time
import copy

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 22 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split('\n\n')
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    deck1 = [int(x) for x in inputs[0].split('\n')[1:]]
    deck2 = [int(x) for x in inputs[1].split('\n')[1:]]

    while not (len(deck1) == 0 or len(deck2) == 0):
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card2 > card1:
            deck2.append(card2)
            deck2.append(card1)
    windeck = deck1 if len(deck1) != 0 else deck2
    soln = 0
    for idx, card in enumerate(windeck[::-1]):
        soln += (idx + 1) * card
    return soln

def part_two():
    deck1 = [int(x) for x in inputs[0].split('\n')[1:]]
    deck2 = [int(x) for x in inputs[1].split('\n')[1:]]

    play(deck1, deck2)
    windeck = deck1 if len(deck1) != 0 else deck2
    soln = 0
    for idx, card in enumerate(windeck[::-1]):
        soln += (idx + 1) * card
    return soln

def play(deck1, deck2):
    states1 = []
    states2 = []
    while True:
        if deck1 in states1 or deck2 in states2:
            deck2 = []
            return 1
        else:
            states1.append(copy.deepcopy(deck1))
            states2.append(copy.deepcopy(deck2))
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            ret = play(copy.deepcopy(deck1)[:card1], copy.deepcopy(deck2)[:card2])
            if ret == 1:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
        elif card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card2 > card1:
            deck2.append(card2)
            deck2.append(card1)

        if len(deck1) == 0:
            return 2
        elif len(deck2) == 0:
            return 1

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
