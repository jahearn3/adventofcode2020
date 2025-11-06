# Day 4: Passport Processing

import load_data as ld
import os
import re

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
ans = 0
passports = []
i = 0
passport = {}
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
while i < len(data):
    if len(data[i]) == 0:
        if all(field in passport for field in required_fields):
            ans += 1
        passport = {}
    else:
        kv_pairs = data[i].split(' ')
        for pair in kv_pairs:
            k, v = pair.split(':')
            passport[k] = v
    i += 1

print(ans)

# Part 2
ans = 0
passports = []
i = 0
passport = {}
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
while i < len(data):
    if len(data[i]) == 0:
        if all(field in passport for field in required_fields):
            if (1920 <= int(passport['byr']) <= 2002 and
                    2010 <= int(passport['iyr']) <= 2020 and
                    2020 <= int(passport['eyr']) <= 2030):
                if (('cm' in passport['hgt'] and
                     150 <= int(passport['hgt'][:-2]) <= 193) or
                    ('in' in passport['hgt'] and
                     59 <= int(passport['hgt'][:-2]) <= 76)):
                    if re.match(r'^#[0-9a-f]{6}$', passport['hcl']):
                        ecl_pattern = r'amb|blu|brn|gry|grn|hzl|oth'
                        if len(re.findall(ecl_pattern, passport['ecl'])) == 1:
                            if re.match(r'^\d{9}$', passport['pid']):
                                ans += 1
        passport = {}
    else:
        kv_pairs = data[i].split(' ')
        for pair in kv_pairs:
            k, v = pair.split(':')
            passport[k] = v
    i += 1

print(ans)
