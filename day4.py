
import re
from aocd import submit
from aocd import get_data

input = get_data(day=4, year=2020)
passports = [x for x in input.split('\n\n')]

valid_a, valid_b = (0, 0)
for passport in passports:
    if passport.count(':') == 8 or (passport.count(':') == 7 and 'cid' not in passport):
        valid_a += 1

        # Check rules
        byr = 1920 <= int(re.search('byr:(\d{4})', passport)[1]) <= 2002
        iyr = 2010 <= int(re.search('iyr:(\d{4})', passport)[1]) <= 2020
        eyr = 2020 <= int(re.search('eyr:(\d{4})', passport)[1]) <= 2030
        hcl = re.search('hcl:#[\da-f]{6}', passport)
        ecl = re.search('ecl:(?:amb|blu|brn|gry|grn|hzl|oth)', passport)
        pid = re.search('pid:\d{9}\\b', passport)
        hgt = re.search('hgt:(\d*)(in|cm)', passport)

        if byr and iyr and eyr and hcl and ecl and pid and hgt:
            if (hgt[2] == 'cm' and 150 <= int(hgt[1]) <= 193) or (hgt[2] == 'in' and 59 <= int(hgt[1]) <= 76):
                valid_b += 1
                #print(passport,'\n')

print(valid_a)
#submit(valid_a, part="a", day=4, year=2020)

print(valid_b)
#submit(valid_b, part="b", day=4, year=2020)
