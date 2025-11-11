# Day 8: Handheld Halting

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
accumulator = 0
i = 0
visited = []
while i < len(data) and i not in visited:
    if i in visited:
        break
    line = data[i]
    operation, argument = line.split(' ')
    if operation == 'acc':
        accumulator += int(argument)
    visited.append(i)
    if operation == 'jmp':
        i += int(argument)
    else:
        i += 1

print(accumulator)

# Part 2


def run_the_program(modified_data):
    accumulator = 0
    i = 0
    visited = []
    while i < len(modified_data) and i not in visited:
        if i in visited:
            return 0
        line = modified_data[i]
        operation, argument = line.split(' ')
        if operation == 'acc':
            accumulator += int(argument)
        visited.append(i)
        if operation == 'jmp':
            i += int(argument)
        else:
            i += 1
    if i == len(modified_data):
        return accumulator
    else:
        return 0


for i, line in enumerate(data):
    operation, argument = line.split(' ')
    if operation != 'acc':
        if operation == 'jmp':
            operation = 'nop'
        elif operation == 'nop':
            operation = 'jmp'
        else:
            print('unknown', operation)
            break
        modified_data = data.copy()
        modified_data[i] = f"{operation} {argument}"
        accumulator = run_the_program(modified_data)
        if accumulator != 0:
            print(accumulator)
            break
