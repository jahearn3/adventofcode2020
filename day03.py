# Day 3: Toboggan Trajectory

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
x, y = 0, 0
ans = 0
for line in data:
    char = data[y][x % len(line)]
    if char == '#':
        ans += 1
    x += 3
    y += 1
print(ans)

# Part 2
n_trees = []
slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]
for slope in slopes:
    dx, dy = slope
    x, y = 0, 0
    n = 0
    while y < len(data):
        char = data[y][x % len(line)]
        if char == '#':
            n += 1
        x += dx
        y += dy
    n_trees.append(n)
ans = 1
for i in n_trees:
    ans *= i
print(ans)
