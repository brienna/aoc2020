
from aocd import submit
from aocd import get_data

input = get_data(day=2, year=2020)
#print(len(input))

records = input.split('\n')
passwords = [x.split(': ')[1] for x in records]
rules = [x.split(': ')[0] for x in records]
total = 0
for idx, rule in enumerate(rules):
    #print(rule)
    letter = rule.split(' ')[1]
    #print("checking letter " + letter)
    letter_appearances = passwords[idx].count(letter)
    #print(passwords[idx])
    #print(letter, "appears... ", letter_appearances)
    min = int(rule.split(' ')[0].split('-')[0])
    max = int(rule.split(' ')[0].split('-')[1])
    #print("min: ", min)
    #print("max: ", max)
    #print(passwords[min])
    print(passwords[idx])
    print(min)
    print(rule)
    print(passwords[idx][min])

    # if password[min] is the letter
    if passwords[idx][min - 1] == letter: # if 1st place has letter
        try:
            if passwords[idx][max - 1] != letter: # test if 2nd place has letter
                total = total + 1 # if it doesn't, perfect
            else:
                continue
        except:
            total = total + 1 # exception if its not that long, ok too
    else:
        try:
            if passwords[idx][max - 1] == letter: # if 2nd place has letter and 1st doesnt
                total = total + 1
            else:
                continue
        except:
            continue

    #if letter_appearances >= min and letter_appearances <= max:
        #total = total + 1

print(total)




# Submit
#submit(total, part="b", day=2, year=2020)




