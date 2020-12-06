
from aocd import submit
from aocd import get_data

input = get_data(day=6, year=2020)
total_yes_a, total_yes_b = (0, 0)
for group in [x for x in input.split('\n\n')]:
    # part a
    total_yes_a += len(set(''.join(group.split('\n'))))

    # part b
    answers = group.split('\n')
    total_yes_b += len(set(answers[0]).intersection(*answers[1:]))

print(total_yes_a)
#submit(total_yes_a, part="a", day=6, year=2020)

print(total_yes_b)
#submit(total_yes_b, part="b", day=6, year=2020)