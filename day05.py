# Day 5: Binary Boarding

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
nrows = 128
seat_ids = []

for line in data:
    min_row, max_row = 0, 127
    min_col, max_col = 0, 7
    row, col = None, None
    for i, char in enumerate(line):
        if i < 7:
            half = ((max_row - min_row + 1) // 2)
            if char == 'F':
                max_row -= half
            elif char == 'B':
                min_row += half
            else:
                print('Error 1')
        else:
            half = ((max_col - min_col + 1) // 2)
            if min_row == max_row:
                row = min_row
            if char == 'L':
                max_col -= half
            elif char == 'R':
                min_col += half
            else:
                print('Error 2')
    if min_col == max_col:
        col = min_col
    if row is not None and col is not None:
        seat_id = row * 8 + col
        seat_ids.append(seat_id)

print(max(seat_ids))

# Part 2
empty_seats = []
for i in range(max(seat_ids)):
    if i not in seat_ids:
        empty_seats.append(i)
print(max(empty_seats))
