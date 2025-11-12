# Day 9: Encoding Error

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

preamble = 25
q = []

for i, line in enumerate(data):
    n = int(line)
    if i < preamble:
        q.append(n)
    else:
        adding = True
        i = 0
        j = 0
        while adding and i < preamble and j < preamble:
            if i != j:
                if q[i] + q[j] == n:
                    # print(f'{q[i]}+{q[j]}={n}')
                    q.pop(0)
                    q.append(n)
                    adding = False
            if i + 1 < preamble:
                i += 1
            elif i + 1 == preamble:
                i = 0
                j += 1
        if q[-1] != n:
            invalid_number = n
            print(n)
            q.pop(0)
            q.append(n)

# Part 2
encryption_weakness = 0
n_set = 2
while encryption_weakness == 0:
    q = []
    for i, line in enumerate(data):
        n = int(line)
        if i < n_set:
            q.append(n)
        else:
            tot = 0
            for j in range(n_set):
                tot += q[j]
            if tot == invalid_number:
                encryption_weakness = min(q) + max(q)
            q.pop(0)
            q.append(n)

    n_set += 1
print(encryption_weakness)
