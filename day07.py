# Day 7: Handy Haversacks

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"example{day}b.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
bags = {}
for line in data:
    k, v = line.split(' bags contain ')
    vv = v.strip('.').split(', ')
    if vv[0] != 'no other bags':
        for i in range(len(vv)):
            words = vv[i].split(' ')
            color = ' '.join(words[1:3])
            if color not in bags:
                bags[color] = []
            bags[color].append(k)

valid_outermost_bags = []
q = bags['shiny gold']

while q:
    bag = q.pop(0)
    if bag not in valid_outermost_bags:
        valid_outermost_bags.append(bag)
    if bag in bags:
        for i in bags[bag]:
            q.append(i)

print(len(valid_outermost_bags))

# Part 2
bags = {}
for line in data:
    k, v = line.split(' bags contain ')
    vv = v.strip('.').split(', ')
    if 'no other bags' in vv:
        bags[k] = [{'count': 0, 'color': None}]
    else:
        bags[k] = []
        for i in range(len(vv)):
            words = vv[i].split(' ')
            qty = int(words[0])
            color = ' '.join(words[1:3])
            bags[k].append({'count': qty, 'color': color})


def bags_in_bags(bags, parent):
    if parent is None:
        return 0
    else:
        parent = bags[parent]

    total = 0
    for child in parent:
        total += child['count'] * (bags_in_bags(bags, child['color']) + 1)

    return total


print(bags_in_bags(bags, 'shiny gold'))
