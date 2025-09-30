import re

handle = open("regex_sum_42.txt")
total = 0

for line in handle:
    numbers = re.findall('[0-9]+',line)
    for number in numbers:
        total += int(number)
print(total)    