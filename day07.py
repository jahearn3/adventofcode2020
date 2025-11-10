# Day 7: Handy Haversacks

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
# data = ld.load_data(f"input{day}.txt")

# Part 1
bags = {}
sgab = {}
for line in data:
    k, v = line.split(' bags contain ')
    vv = v.strip('.').split(', ')
    if 'no other bags' in vv:
        bags[k] = []
    else:
        bags[k] = []
        for i in range(len(vv)):
            words = vv[i].split(' ')
            color = ' '.join(words[1:3])
            bags[k].append(color)
            if color not in sgab:
                sgab[color] = []
            sgab[color].append(k)


# for k, v in bags.items():
#     print(k, v)

# for k, v in sgab.items():
#     print(k, v)

# Go through dictionary from shiny gold
valid_outermost_bags = []
q = sgab['shiny gold']

while q:
    bag = q.pop(0)
    # print('bag:', bag)
    if bag not in valid_outermost_bags:
        # print('Adding', bag, 'to valid_outermost_bags')
        valid_outermost_bags.append(bag)
    if bag in sgab:
        for i in sgab[bag]:
            # print('Adding', i, 'to q')
            q.append(i)
    # else:
        # print(bag, 'not in sgab')

# print(valid_outermost_bags)
print(len(valid_outermost_bags))

# Part 2
bags = {}
# sgab = {}
for line in data:
    k, v = line.split(' bags contain ')
    vv = v.strip('.').split(', ')
    if 'no other bags' in vv:
        bags[k] = []
    else:
        bags[k] = []
        for i in range(len(vv)):
            words = vv[i].split(' ')
            qty = int(words[0])
            color = ' '.join(words[1:3])
            bags[k].append((color, qty))
            # if color not in sgab:
            #     sgab[color] = []
            # sgab[color].append(k)


for k, v in bags.items():
    print(k, v)

# for k, v in sgab.items():
#     print(k, v)

# Go through dictionary from shiny gold
seen = []
bags_required = 1
q = bags['shiny gold']

while q:
    bag = q.pop(0)
    (b, qty) = bag
    # print('bag:', bag)
    # if bag not in seen:
    #     # print('Adding', bag, 'to valid_outermost_bags')
    #     seen.append(bag)
    # if bag in bags:
    #     for i in sgab[bag]:
    #         # print('Adding', i, 'to q')
    #         q.append(i)
    if len(bags[b]) > 0:
        for i in bags[b]:
            (bb, qt) = i
            bags_required += (qty * qt)
            print(b, bb, qty, qt)
            q.append(i)

print(bags_required)
