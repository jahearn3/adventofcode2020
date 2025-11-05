# Day 1: Report Repair

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
for a in data:
    for b in data:
        if int(a) + int(b) == 2020:
            ans = int(a) * int(b)

print(ans)

# Part 2
for a in data:
    for b in data:
        for c in data:
            if int(a) + int(b) + int(c) == 2020:
                ans = int(a) * int(b) * int(c)

print(ans)
