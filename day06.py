# Day 6: Custom Customs

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
ans = 0
grp = []
for line in data:
    if len(line) == 0:
        ans += len(set(grp))
        grp = []
    else:
        for char in line:
            grp.append(char)
ans += len(set(grp))
print(ans)


# Part 2
def count_common_chars(grp):
    count = 0
    if len(grp) == 1:
        count += len(set(grp[0]))
    else:
        for char in grp[0]:
            go = True
            for i in grp[1:]:
                if char not in i:
                    go = False
            if go:
                count += 1
    return count


ans = 0
grp = []
ind = []
for line in data:
    if len(line) == 0:
        ans += count_common_chars(grp)
        grp = []
    else:
        for char in line:
            ind.append(char)
        grp.append(ind)
    ind = []
ans += count_common_chars(grp)
print(ans)
