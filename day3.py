
# rows = [list(x) for x in input.split('\n')
# ^ this can be removed, along with other input formatting statements

from aocd import submit
from aocd import get_data

input = get_data(day=3, year=2020)
rows = [list(x) for x in input.split('\n')]

def ride(right, down):
    rowIndex, col, trees = (0, 0, 0)
    while rowIndex < len(rows):
        if rows[rowIndex][col] == '#':
            trees += 1
            #rows[rowIndex][col] = 'X'
        #else:
            #rows[rowIndex][col] = 'O'

        #print(''.join(rows[rowIndex]))
        rowIndex += down
        col = (col + right) % len(rows[0])
    return trees

a = ride(3, 1)
print(a)

b = ride(1, 1) * a * ride(5, 1) * ride(7, 1) * ride(1, 2)
print(b)

#submit(b, part="b", day=3, year=2020)

