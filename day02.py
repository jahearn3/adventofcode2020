# Day 2: Password Philosophy

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
ans = 0

for line in data:
    policy, password = line.split(':')
    minmax, letter = policy.split(' ')
    min, max = minmax.split('-')
    min, max = int(min), int(max)
    count = 0
    for char in password:
        if char == letter:
            count += 1
    if min <= count <= max:
        ans += 1

print(ans)

# Part 2
ans = 0

for line in data:
    policy, password = line.split(':')
    password = password.strip()
    positions, letter = policy.split(' ')
    i, j = positions.split('-')
    i, j = int(i), int(j)
    count = 0
    if password[i-1] == letter:
        count += 1
    if password[j-1] == letter:
        count += 1
    if count == 1:
        ans += 1

print(ans)
