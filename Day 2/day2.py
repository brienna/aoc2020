
from aocd import submit
from aocd import get_data

input = get_data(day=2, year=2020)
rules, passwords = map(list, zip(*(x.split(': ') for x in input.split('\n'))))

def check_passwords(which_part):
    total = 0
    for idx, rule in enumerate(rules):
        letter = rule.split(' ')[1]
        num_occurrences = passwords[idx].count(letter)
        min, max = map(int, rule.split(' ')[0].split('-'))

        if which_part == 'a':
            if min <= num_occurrences <= max:
                total += 1
        elif which_part == 'b':
            if passwords[idx][min - 1] == letter and passwords[idx][max - 1] != letter:
                total += 1
            if passwords[idx][min - 1] != letter and passwords[idx][max - 1] == letter:
                total += 1
    return total

total = check_passwords('a')
print('Total for part A: ', total)
#submit(total, part="a", day=2, year=2020)

total = check_passwords('b')
print('Total for Part B: ', total)
#submit(total, part="b", day=2, year=2020)



