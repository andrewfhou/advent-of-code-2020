import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 09 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
# with open("example.txt") as file:
    inputs = file.read().strip().split('\n')
    inputs = [int(x) for x in inputs]
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one():
    for i in range(25, len(inputs)):
        prev = inputs[(i - 25):i]
        valid = False
        for x in range(25):
            for y in range(25):
                if prev[x] + prev[y] == inputs[i]:
                    valid = True
        if not valid:
            return inputs[i]

def part_two():
    vuln = part_one()
    vals = dict()
    runsum = 0
    for i in range(len(inputs)):
        vals[runsum] = i
        runsum += inputs[i]
        if (runsum - vuln) in vals:
            return min(inputs[vals[runsum - vuln]:(i + 1)]) + max(inputs[vals[runsum - vuln]:(i + 1)])

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
