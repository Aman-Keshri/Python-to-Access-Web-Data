import re

file = open('regex_sum_906447.txt.txt', 'r')

s = 0

for line in file:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        s = s + int(number)

print(s)