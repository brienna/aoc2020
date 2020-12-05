

from math import floor, ceil
from aocd import submit
from aocd import get_data

input = get_data(day=5, year=2020)
seats = [x for x in input.split('\n')]

seat_ids = []
#for seat in seats:
for seat in seats:
    #print(seat)
    row = [0, 127]
    for partition in seat[:7]:
        if partition == 'F': # lower
            row[1] = floor(row[1] - (row[1]-row[0]) / 2)
        elif partition == 'B': # upper
            row[0] = ceil((row[1]+row[0]) / 2)

    #print('row:', row)

    column = [0, 7]
    print()
    for partition in seat[7:]:
        #print(partition)
        if partition == 'L': # lower half

            column[1] = floor(column[1] - ((column[1] - column[0]) / 2))

        elif partition == 'R': # upper half
            column[0] = ceil((column[1]+column[0]) / 2)
    print('column:', column)
    #print()

    seat_id = row[0] * 8 + column[0]
    #print(seat_id)
    #print(seat_id in seat_ids)
    seat_ids.append(seat_id)

#print(max(seat_ids))

# part b
def find_missing(lst):
    lst = sorted(lst)
    start = min(lst)
    end = max(lst)
    return sorted(set(range(start, end + 1)).difference(lst))


print(find_missing(seat_ids))





#print(valid_a)
#submit(max(seat_ids), part="a", day=5, year=2020)

#print(valid_b)
submit(find_missing(seat_ids), part="b", day=5, year=2020)
