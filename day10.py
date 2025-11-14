# Day 10: Adapter Array

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"example{day}b.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
adapters = [int(line) for line in data]
sorted_adapters = sorted(adapters)

j1 = 0
j3 = 0
j = 0

for a in sorted_adapters:
    diff = a - j
    if diff == 1:
        j1 += 1
    elif diff == 3:
        j3 += 1
    if diff < 4:
        j = a
    else:
        print('Joltage difference error!', j, a)
j3 += 1

print(j1 * j3)

# Part 2
